# Python Secure Coding Guide - Rule Overview Draft

This table provides an overview of all pyscg rules with their current titles, space for new titles, and the first sentence and paragraph from each rule's README.md.

<table border="1">
<tr>
<th>pyscg ID</th>
<th>Current Title</th>
<th>New Title</th>
<th>CWE</th>
<th>First Sentence</th>
<th>First Paragraph</th>
</tr>

<tr>
<th colspan="6" style="text-align: left; padding: 10px;">
<h3 style="margin: 0;">01 Introduction</h3>
</th>
</tr>

<tr>
<td><a href="01_introduction/pyscg-0040/README.md">pyscg-0040</a></td>
<td>Trust Boundary Violation</td>
<td>Use Process Isolation for Trust Zones</td>
<td><a href="https://cwe.mitre.org/data/definitions/501.html">CWE-501</a></td>
<td>Python's trust boundaries rely on explicit process isolation, rather than in-process access control within a single interpreter.<br>
<b>Change to:</b><br>
Create isolated trust zones on the operating system level.
</td>
<td>Unlike Java, where we have in-process mechanisms like <a href="https://docs.oracle.com/en/middleware/idm/access-manager/12.2.1.3/aiaag/introducing-oracle-access-management.html">Oracle Access Management</a> that can enforce access boundaries inside the same runtime, standard Python does not provide a built-in in-process access manager. In Python we need to implement different trust zones by starting python runtimes with individual POSIX/Machine users. The POSIX/Machine user access rights must be set in accordance to level of trust per zone.</td>
</tr>

<tr>
<td><a href="01_introduction/pyscg-0041/README.md">pyscg-0041</a></td>
<td>Use of Hardcoded Credentials</td>
<td>Externalize Configuration and Secrets</td>
<td><a href="https://cwe.mitre.org/data/definitions/798.html">CWE-798</a></td>
<td>Ensure that unique keys or secrets can be replaced or rejected at runtime and never hard-code sensitive information, such as passwords, and encryption keys in a component.</td>
<td>User accounts are either for human or machine type of users. Machine users, such as a front end connecting to a backend <code>SQL</code>, have it easy to use complexity during identity verification. Hardcoded credentials for machine users are typically caused by a missing strategy or architecture infrastructure to establish trust between components at deployment time. Human users need a level of usability for their identity verification such as a combination of what they have and what they can remember. A human user Identity Management (IDM) system needs to support initial access and users forgetting passphrases or passwords without jeopardizing security.</td>
</tr>

<tr>
<td><a href="01_introduction/pyscg-0042/README.md">pyscg-0042</a></td>
<td>Operator Precedence Logic Error</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/783.html">CWE-783</a></td>
<td>Failing to understand the order of precedence in expressions that read and write to the same object can lead to unintended side effects.</td>
<td>Python has distinct different concepts for:</td>
</tr>

<tr>
<td><a href="01_introduction/pyscg-0055/README.md">pyscg-0055</a></td>
<td>External Control of Assumed-Immutable Web Parameter</td>
<td>Determine Access on Server Side</td>
<td><a href="https://cwe.mitre.org/data/definitions/472.html">CWE-472</a></td>
<td>Ensuring user roles are determined on the server side prevents attackers from manipulating permissions through client-side data.</td>
<td></td>
</tr>

<tr>
<th colspan="6" style="text-align: left; padding: 10px;">
<h3 style="margin: 0;">02 Encoding and Strings</h3>
</th>
</tr>

<tr>
<td><a href="02_encoding_and_strings/pyscg-0043/README.md">pyscg-0043</a></td>
<td>Improper Handling of Mixed Encoding</td>
<td>Specify Locale Explicitly<br>
<b>TODO:</b><br>
move the encoding examples into the encoding 0045 rule.</td>
<td><a href="https://cwe.mitre.org/data/definitions/175.html">CWE-175</a></td>
<td>Locale-dependent programs may produce unexpected behavior or security bypasses in an environment whose locale is unset, or not set to an appropriate value.</td>
<td>In Python, the <code>locale</code> module will never perform case conversions or character classifications according to the locale <a href="https://docs.python.org/3.9/library/locale.html">[Python 3.9 locale]</a>. Python follows the Unicode conventions for text <a href="https://bugs.python.org/issue34928">[Python Issue 34928]</a>, and this behavior may not match the user's expectation in their native language. Some characters, such as the German ß (eszett), Greek Σ (sigma) also have particular rules in Unicode that may not match native usage and need to be handled carefully. Also, be aware of differences in other languages that use right-to-left ordering (e.g. Arabic) and languages which use CJK characters.</td>
</tr>

<tr>
<td><a href="02_encoding_and_strings/pyscg-0044/README.md">pyscg-0044</a></td>
<td>Incorrect Behavior Order: Validate Before Canonicalize</td>
<td>Canonicalize Input Before Validating</td>
<td><a href="https://cwe.mitre.org/data/definitions/180.html">CWE-180</a></td>
<td>Normalize/canonicalize strings before validating them to prevent risky strings such as  <code>../../../../passwd</code> allowing directory traversal attacks, and to reduce <code>XSS</code> attacks.</td>
<td>The need for supporting multiple languages requires the use of an extended list of characters encoding such as <code>UTF-8</code> supporting <strong>1,112,064</strong> displayable characters.</td>
</tr>

<tr>
<td><a href="02_encoding_and_strings/pyscg-0045/README.md">pyscg-0045</a></td>
<td>Collapse of Data into Unsafe Value</td>
<td>Enforce Consistent Encoding<br><br>
<b>TODO:</b><br>
change CWE to CWE-176: Improper Handling of Unicode Encoding</td>
<td><a href="https://cwe.mitre.org/data/definitions/182.html">CWE-182</a></td>
<td>Handling data between different encodings or while filtering out untrusted characters and strings can cause malicious content to slip through input sanitation.</td>
<td>Encoding changes, such as changing from <code>UTF-8</code> to pure <code>ASCII</code>, can result in turning non-functional payloads, such as <code>&lt;script生&gt;</code>, into functional <code>&lt;script&gt;</code> tags. Mixed encoding modes <a href="02_encoding_and_strings/pyscg-0044/README.md">pyscg-0044: Incorrect behavior order: Validate before Canonicalize</a> can also play a role. The recommendation by <a href="https://www.youtube.com/watch?v=sgHbC6udIqc">Batchelder 2022</a> to use a single type of encoding and mode is only applicable for a single project or supplier. The recommendation to always choose the <code>UTF-8</code> by <a href="https://www.w3.org/International/questions/qa-what-is-encoding">W3c.org 2025</a> provides no guarantee and is already flawed by Windows having <code>Windows-1252</code> encoding for some Python installations.</td>
</tr>

<tr>
<td><a href="02_encoding_and_strings/pyscg-0046/README.md">pyscg-0046</a></td>
<td>Inappropriate Encoding for Output Context</td>
<td>Merge knowledge into into 0045</td>
<td><a href="https://cwe.mitre.org/data/definitions/838.html">CWE-838</a></td>
<td>Inappropriate handling of an encoding from untrusted sources or unexpected encoding can lead to unexpected values, data loss, or become the root cause of an attack.</td>
<td>Mixed encoding can lead to unexpected results and become a root cause for attacks as showcased in <a href="02_encoding_and_strings/pyscg-0044/README.md">pyscg-0044: Incorrect Behavior Order: Validate Before Canonicalize</a> and <a href="../pyscg-0043/README.md">pyscg-0043: Improper Handling Of Mixed Encoding</a> This rule showcases capturing the root cause by untrusted source its original binary without compromising the logging system for forensics.</td>
</tr>

<tr>
<th colspan="6" style="text-align: left; padding: 10px;">
<h3 style="margin: 0;">03 Numbers</h3>
</th>
</tr>

<tr>
<td><a href="03_numbers/pyscg-0001/README.md">pyscg-0001</a></td>
<td>Insufficient Precision or Accuracy of a Real Number</td>
<td>Control Numeric Precision<br><br>
Note: check if we correctly talk about Real vs other types of numbers in the rule</td>
<td><a href="https://cwe.mitre.org/data/definitions/1339.html">CWE-1339</a></td>
<td>Avoid floating-point and use integers or the <code>decimal</code> module to ensure precision in applications that require high accuracy, such as in financial or banking computations.</td>
<td>In Python, floating-point types are constrained by a fixed number of binary mantissa bits, typically allowing for around seven decimal digits of precision (24-bit values). Consequently, they are not well-suited for representing surds, such as <code>√7</code> or <code>π</code> with full accuracy. Additionally, due to their binary nature, floating-point types are incapable of exactly terminating decimals in <code>base 10</code>, such as <code>0.3</code>, which has a repeating binary representation.</td>
</tr>

<tr>
<td><a href="03_numbers/pyscg-0002/README.md">pyscg-0002</a></td>
<td>Integer Underflow ('Wrap or Wraparound')</td>
<td>Guard C-Backed Numbers Against Overflow<br><br>
TODO: explain what we mean by c-backed numebers in the rule.</td>
<td><a href="https://cwe.mitre.org/data/definitions/191.html">CWE-191</a></td>
<td>Ensure that integer overflow is properly handled in order to avoid unexpected behavior.</td>
<td>Python data types can be divided into two categories: - Built-in types such as <code>int</code>, <code>float</code>, or <code>complex</code> <a href="https://docs.python.org/3.9/library/stdtypes.html">[Python 2024]</a>. These types are provided by classes and are protected against overflows.</td>
</tr>

<tr>
<td><a href="03_numbers/pyscg-0053/README.md">pyscg-0053</a></td>
<td>Incorrect Bitwise Shift of Integer</td>
<td>TODO: merge knowledge into 0003 and remove.</td>
<td><a href="https://cwe.mitre.org/data/definitions/1335.html">CWE-1335</a></td>
<td>Avoid mixing bitwise shifts with arithmetic operations, instead, use clear mathematical expressions instead to maintain predictable behavior, readability, and compatibility.</td>
<td>Ensure to know what bit-wise shift operators do in case you can not avoid them as recommended in <em>NUM01-J. Do not perform bitwise and arithmetic operations on the same data</em> <a href="https://wiki.sei.cmu.edu/confluence/display/java/NUM01-J.+Do+not+perform+bitwise+and+arithmetic+operations+on+the+same+data">[SEI CERT JAVA 2024]</a> and use math instead.</td>
</tr>

<tr>
<td><a href="03_numbers/pyscg-0003/README.md">pyscg-0003</a></td>
<td>Promote Readability and Compatibility by Using Mathematical Written Code with Arithmetic Operations Instead of Bit-wise Operations</td>
<td>Use Arithmetic Over Bitwise Operations<br><br>
TODO: merge 0053 required knowledge into 0003</td>
<td><a href="https://cwe.mitre.org/data/definitions/1335.html">CWE-1335</a></td>
<td>Avoid using bitwise operations for calculations, write math as math instead to ensure code clarity, compatibility and maintainability.</td>
<td><code>C</code> and <code>C++</code> used to have two design patterns in order to optimize resource utilization:</td>
</tr>

<tr>
<td><a href="03_numbers/pyscg-0004/README.md">pyscg-0004</a></td>
<td>Numeric Truncation Error</td>
<td>Use Integer Loop Counters</td>
<td><a href="https://cwe.mitre.org/data/definitions/197.html">CWE-197</a></td>
<td>Ensure to have predictable outcomes in loops by using int instead of <code>float</code> variables as a counter.</td>
<td>Floating-point arithmetic can only represent a finite subset of real numbers <a href="https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8766229">[IEEE Std 754-2019]</a>, such as <code>0.555....</code> represented by <code>0.5555555555555556</code> also discussed in <a href="../pyscg-0001/README.md">pyscg-0001: Insufficient Precision Or Accuracy Of A Real Number</a>. Code examples in this rule are based on [Albing and Vossen, 2017].</td>
</tr>

<tr>
<td><a href="03_numbers/pyscg-0005/README.md">pyscg-0005</a></td>
<td>Control Rounding When Converting to Less Precise Numbers</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/197.html">CWE-197</a></td>
<td>While defensive coding requires enforcing types, it is important to make conscious design decisions on how conversions are rounded.</td>
<td>The <code>example01.py</code> code demonstrates how <code>int()</code> behaves differently to <code>round()</code>.</td>
</tr>

<tr>
<td><a href="03_numbers/pyscg-0006/README.md">pyscg-0006</a></td>
<td>Incorrect Conversion Between Numeric Types</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/681.html">CWE-681</a></td>
<td>String representations of floating-point numbers must not be compared or inspected outside of specialized modules such as <code>decimal</code> or <code>math</code>.</td>
<td>For example, a <code>Decimal</code> object must be created from a <code>string</code>, but it is inaccurate to use the string representation of a floating-point number outside of <code>Decimal</code>. The <code>Decimal</code> module provides a <code>compare()</code> method that allows the calculation to stay within its configured precision.</td>
</tr>

<tr>
<td><a href="03_numbers/pyscg-0007/README.md">pyscg-0007</a></td>
<td>Avoid an Uncontrolled Loss of Precision When Passing Floating-point Literals to a Decimal Constructor</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/681.html">CWE-681</a></td>
<td>When working with decimal numbers in Python, using floating-point literals as input to the <code>Decimal</code> constructor can lead to unintended imprecision due to the limitations of <code>IEEE 754</code> <a href="https://en.wikipedia.org/wiki/IEEE_754">Wikipedia 2025</a> floating-point representation; therefore, to ensure accurate decimal representation, it is advisable to avoid using floating-point literals.</td>
<td></td>
</tr>

<tr>
<th colspan="6" style="text-align: left; padding: 10px;">
<h3 style="margin: 0;">04 Neutralization</h3>
</th>
</tr>

<tr>
<td><a href=04_neutralization/pyscg-0047/README.md>pyscg-0047</a></td>
<td>Incomplete List of Disallowed Input</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/184.html">CWE-184</a></td>
<td>Avoid Incomplete 'deny lists' that can lead to security vulnerabilities such as cross-site scripting (XSS) by using 'allow lists' instead.</td>
<td></td>
</tr>

<tr>
<td><a href="04_neutralization/pyscg-0008/README.md">pyscg-0008</a></td>
<td>Use of Externally-Controlled Format String</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/134.html">CWE-134</a></td>
<td>Ensure that all format string functions are passed a static string which cannot be controlled by the user <a href="https://cwe.mitre.org/data/definitions/134.html">[MITRE 2023]</a></td>
<td>In Python, the use of string formatting combined with the ability to access a function's <code>__globals__</code> attribute can expose internal variables and methods unless properly guarded.</td>
</tr>

<tr>
<td><a href="04_neutralization/pyscg-0009/README.md">pyscg-0009</a></td>
<td>Improper Neutralization of Special Elements Used in an OS Command ('OS Command Injection')</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/78.html">CWE-78</a></td>
<td>Avoid input from untrusted sources to be used directly as part of an OS command and use specialized Python modules where possible instead.</td>
<td>Python can run shell commands either with an active <code>shell=True</code> where an actual shell is invoked to run a line of commands such <code>/bin/bash -c "ls -la *.txt"</code> or via non-interactive <code>shell=False</code> expecting a Python list object.</td>
</tr>

<tr>
<td><a href=04_neutralization/pyscg-0010/README.md>pyscg-0010</a></td>
<td>Improper Neutralization of Special Elements Used in an SQL Command ('SQL Injection')</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/89.html">CWE-89</a></td>
<td>To prevent SQL injections, use input sanitization and parameterized queries instead of <code>executescript()</code>.</td>
<td>Combining an SQL query with data from lesser trusted sources, such as fields from a web form used to sign up new clients, can allow an attacker to inject malicious SQL statements.</td>
</tr>

<tr>
<td><a href=04_neutralization/pyscg-0011/README.md>pyscg-0011</a></td>
<td>Access of Resource Using Incompatible Type ('Type Confusion')</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/843.html">CWE-843</a></td>
<td>When operating on unsigned values coming from external sources, such as <code>C</code> or <code>C++</code> applications, they should be unpacked using variable types that can represent their entire value range.</td>
<td>This rule is related to <a href="../../03_numbers/pyscg-0005/README.md">pyscg-0005: Control Rounding When Converting to Less Precise Numbers</a>.</td>
</tr>

<tr>
<td><a href=04_neutralization/pyscg-0012/README.md>pyscg-0012</a></td>
<td>Improper Handling of Highly Compressed Data ('Data Amplification')</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/409.html">CWE-409</a></td>
<td>Prevent slip and bomb attacks when decompressing and unpacking compressed data such as <code>ZIP</code>, <code>TAR.GZ</code>, <code>JAR</code>, <code>WAR</code>, <code>RPM</code>  or <code>DOCX</code>.</td>
<td>Zip is used reprehensively in this rule for all compression formats.</td>
</tr>

<tr>
<td><a href=04_neutralization/pyscg-0013/README.md>pyscg-0013</a></td>
<td>Untrusted Search Path</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/426.html">CWE-426</a></td>
<td>In an environment where an untrusted or less trusted entity can modify the environment variables, consider validating hash-based byte code [Python 2023 Command line and environment].</td>
<td>Python source code <code>.py</code> files need to be converted into "byte code" <code>.pyc</code> or <code>.pyo</code> in memory or in a filesystem <code>__pycache__</code> before running on the Python Virtual Machine (PVM) [Dec 2009 PEP 3147].</td>
</tr>

<tr>
<td><a href=04_neutralization/pyscg-0023/README.md>pyscg-0023</a></td>
<td>Deserialization of Untrusted Data</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/502.html">CWE-502</a></td>
<td>Even if data has been created from a trusted source, we need to verify that it has not been tampered with during transport.</td>
<td>The <code>pickle</code> module is known to be vulnerable <a href="https://docs.python.org/3.9/library/pickle.html">[docs.python.org 2023]</a> against unwanted code execution during deserialization and should only be used if there is no architectural text-based alternative.</td>
</tr>

<tr>
<th colspan="6" style="text-align: left; padding: 10px;">
<h3 style="margin: 0;">05 Exception handling</h3>
</th>
</tr>

<tr>
<td><a href=05_exception_handling/pyscg-0014/README.md>pyscg-0014</a></td>
<td>Declaration of Throws for Generic Exception</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/397.html">CWE-397</a></td>
<td>Avoid raising exceptions that aren't informative on specific errors.</td>
<td><code>Exception</code> is the base class of all non-system-exiting exceptions <a href="https://docs.python.org/3/library/exceptions.html#Exception">[Python docs 2025]</a>. Specific exceptions allow to determine why they were raised and attempt recovery. To catch a generic <code>Exception</code>, you must also account for any more specific exceptions that inherit from it. Raising <code>Exception</code> is likely to hide bugs and and prevents using more specialized except statements. The problem is even more severe when raising <code>BaseException</code>, which additionally includes subclasses signifying termination signals, such as <code>KeyboardInterrupt</code> and <code>SystemExit</code> <a href="https://peps.python.org/pep-0352/#exception-hierarchy-changes">[PEP 2024]</a>.</td>
</tr>

<tr>
<td><a href=05_exception_handling/pyscg-0015/README.md>pyscg-0015</a></td>
<td>Improper Handling of Exceptional Conditions</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/755.html">CWE-755</a></td>
<td>Always catch and explicitly handle exceptions, then respond, log or recover appropriately instead of letting operations fail silently.</td>
<td>There are two built-in Python modules that allow for file manipulation. The original module is called <code>os</code>. It provides the ability to perform various functions related to the operating system, among which are creating, updating, and deleting files <a href="https://docs.python.org/3/library/os.html">[Python docs - os]</a>. Python 3.4 introduced the <code>pathlib</code>  module, which represents file paths as objects as opposed to string variables <a href="https://docs.python.org/3/library/pathlib.html">[Python docs - pathlib]</a>.</td>
</tr>

<tr>
<td><a href=05_exception_handling/pyscg-0016/README.md>pyscg-0016</a></td>
<td>Detection of Error Condition Without Action</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/390.html">CWE-390</a></td>
<td>Allow exceptions to bubble up and handle exceptions at the right level in the stack.</td>
<td>Each <code>except</code> block must ensure that the program continues only with formally specified behavior by either:</td>
</tr>

<tr>
<td><a href=05_exception_handling/pyscg-0017/README.md>pyscg-0017</a></td>
<td>Improper Handling of Missing Values</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/230.html">CWE-230</a></td>
<td>Detect and handle missing numberic values explicitly, either by removing, validating or converting them, before performing comparisons, sorting, or statistics, in order to avoid surprising or undefined behaviour.</td>
<td>The <code>NaN</code> value should be stripped before as they can cause surprising or undefined behaviours in the statistics functions that sort or count occurrences <a href="https://docs.python.org/3/library/statistics.html">[2024 doc.python.org]</a>.</td>
</tr>

<tr>
<td><a href=05_exception_handling/pyscg-0018/README.md>pyscg-0018</a></td>
<td>Improper Check for Unusual or Exceptional Conditions - Float</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/754.html">CWE-754</a></td>
<td>Ensure to have handling for exceptional floating-point values.</td>
<td>The <code>float</code> class has the capability to interpret various input values as floating-point numbers. Some special cases can interpret input values as</td>
</tr>

<tr>
<td><a href=05_exception_handling/pyscg-0052/README.md>pyscg-0052</a></td>
<td>Improper Cleanup on Thrown Exception</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/460.html">CWE-460</a></td>
<td>Make sure that your code fully and correctly cleans up its state whenever an exception occurs to avoid unexpected state or control flow.</td>
<td>Often, when functions or loops become complicated, some level of resource cleanup is needed throughout execution.</td>
</tr>

<tr>
<th colspan="6" style="text-align: left; padding: 10px;">
<h3 style="margin: 0;">06 Logging</h3>
</th>
</tr>

<tr>
<td><a href=06_logging/pyscg-0019/README.md>pyscg-0019</a></td>
<td>Insertion of Sensitive Information into Log File</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/532.html">CWE-532</a></td>
<td>Do not log any sensitive information such as passwords or credit card numbers. Encrypt or anonymize personal information such as user names, and date of birth in plain text.</td>
<td>Logging is crucial for tasks like debugging, forensic analysis, and the general management of various incidents, however, it poses significant challenges when it comes to personal information and sensitive information.</td>
</tr>

<tr>
<td><a href=06_logging/pyscg-0020/README.md>pyscg-0020</a></td>
<td>Insufficient Logging</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/778.html">CWE-778</a></td>
<td>Ensure you have sufficient logging in order to adequately record important events within an application and/or system.</td>
<td>Without comprehensive and sufficient logging, it becomes challenging to identify and respond to security incidents, leading to delayed and/or inefficient incident response efforts.</td>
</tr>

<tr>
<td><a href=06_logging/pyscg-0021/README.md>pyscg-0021</a></td>
<td>Active Debug Code</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/489.html">CWE-489</a></td>
<td>Keep design tooling in separate packages from the actual product and supply useful logging.</td>
<td>Design tooling for functional tests, performance tests, or troubleshooting increases the attackable surface making a product more vulnerable <a href="https://cwe.mitre.org/data/definitions/489.html">[MITRE 2023]</a>. A need to include them in a final product typically originates from missing the concept of staged testing with separate packaging of the product and required design tooling. Designers only using high privileged users for troubleshooting is often the root cause for badly designed logging that forces the operator to also use highly privileged or shared accounts in production.</td>
</tr>

<tr>
<td><a href=06_logging/pyscg-0022/README.md>pyscg-0022</a></td>
<td>Improper Output Neutralization for Logs</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/117.html">CWE-117</a></td>
<td>Ensure all untrusted data is properly neutralized or sanitized before writing to application logs.</td>
<td>Log injection occurs when untrusted data is written to application logs without proper neutralization, allowing attackers to forge log entries or inject malicious content. Attackers can inject fake log records or hide real ones by inserting newline sequences (<code>\r</code> or <code>\n</code>), misleading auditors and incident-response teams. This vulnerability can also enable injection of XSS attacks when logs are viewed in vulnerable web applications.</td>
</tr>

<tr>
<td><a href=06_logging/pyscg-0050/README.md>pyscg-0050</a></td>
<td>Generation of Error Message Containing Sensitive Information</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/209.html">CWE-209</a></td>
<td>Prevent an attacker from discovering internal or sensitive system information by filtering, splitting and applying brute force prevention tactics when displaying error messages to a user.</td>
<td>This rule is closely related to <a href="../pyscg-0019/README.md">pyscg-0019: Insertion of Sensitive Information into Log File</a>.</td>
</tr>

<tr>
<th colspan="6" style="text-align: left; padding: 10px;">
<h3 style="margin: 0;">07 Concurrency</h3>
</th>
</tr>

<tr>
<td><a href=07_concurrency/pyscg-0024/README.md>pyscg-0024</a></td>
<td>Uncontrolled Resource Consumption</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/400.html">CWE-400</a></td>
<td>Canceling the task in a thread pool only prevents it from being executed if it has not started yet. For the task to be interruptible, it must handle the <code>threading.Event</code> flag.</td>
<td></td>
</tr>

<tr>
<td><a href=07_concurrency/pyscg-0025/README.md>pyscg-0025</a></td>
<td>Insufficient Resource Pool</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/410.html">CWE-410</a></td>
<td>Ensure load control during traffic bursts or Denial of Service (DoS) by using a limited amount of threads in a pool.</td>
<td>An attacker can cause a DoS by flooding a system with too many requests. Services with time-consuming, I/O-bound, or session-based sequential execution make limited use of available resources and can be blocked by a single hanging process or by overloading the queue.</td>
</tr>

<tr>
<td><a href=07_concurrency/pyscg-0026/README.md>pyscg-0026</a></td>
<td>Deadlock</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/833.html">CWE-833</a></td>
<td>Submitting tasks whose execution is dependent on other tasks submitted to the same <code>ThreadPoolExecutor</code> may result in a <em>thread-starvation</em> deadlock.</td>
<td>The number of threads that can simultaneously run within a <code>ThreadPoolExecutor</code> is limited by the <code>_max_workers</code> parameter. Since <code>Python 3.8</code>, the default value for <code>max_workers</code> is <code>min(32, os.cpu_count() + 4)</code> <a href="https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor">[Python docs]</a>. An example of this type of deadlock is shown in the following article [Brownlee, 2021], which describes it as "Deadlock 1: Submit and Wait for a Task Within a Task". Submitting a task will add it to an internal <code>ThreadPoolExecutor</code> queue. The task will be removed from the queue when one of the worker threads becomes available, i.e., after finishing its current task. If all workers are busy and all their current tasks are waiting for results from tasks that are waiting in the queue, the program will run indefinitely as no worker will be able to complete its task and take one of the blocking tasks from the queue.</td>
</tr>

<tr>
<td><a href=07_concurrency/pyscg-0027/README.md>pyscg-0027</a></td>
<td>Concurrent Execution Using Shared Resource with Improper Synchronization ('Race Condition')</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/362.html">CWE-362</a></td>
<td>Ensure to implement locking mechanisms when chaining methods in a multithreaded environment to prevent unexpected results.</td>
<td>Method chaining is a programming technique where multiple methods are called on the same object sequentially, with each method call returning the object itself or another object that supports further method calls.  Objects that return a reference to themselves allow method chaining, which we frequently use when stripping strings of unwanted content:</td>
</tr>

<tr>
<td><a href=07_concurrency/pyscg-0028/README.md>pyscg-0028</a></td>
<td>Return inside Finally Block</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/584.html">CWE-584</a></td>
<td>Do not use <code>return</code>, <code>break</code> or <code>continue</code> statements in a try-finally block, as the exception will not be processed. The Python documentation <a href="https://docs.python.org/3.9/reference/compound_stmts.html#finally">[Python 3.9]</a> notes, "If the <code>finally</code> clause executes a <a href="https://docs.python.org/3.9/reference/simple_stmts.html#return"><code>return</code></a>, <a href="https://docs.python.org/3.9/reference/simple_stmts.html#break"><code>break</code></a> or <a href="https://docs.python.org/3.9/reference/simple_stmts.html#continue"><code>continue</code></a> statement, the saved exception is discarded."</td>
<td></td>
</tr>

<tr>
<td><a href=07_concurrency/pyscg-0029/README.md>pyscg-0029</a></td>
<td>Improper Initialization</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/665.html">CWE-665</a></td>
<td>Prevent unexpected states by applying correct initialized of local objects as they remain available when a thread's resources are re-used in a thread-pool.</td>
<td></td>
</tr>

<tr>
<td><a href=07_concurrency/pyscg-0030/README.md>pyscg-0030</a></td>
<td>Missing Report of Error Condition</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/392.html">CWE-392</a></td>
<td>Failure to provide a mechanism for reporting that tasks in a thread pool failed as a result of an exceptional condition can make it difficult or impossible to diagnose the problem.</td>
<td></td>
</tr>

<tr>
<td><a href=07_concurrency/pyscg-0051/README.md>pyscg-0051</a></td>
<td>Improper Resource Shutdown or Release</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/404.html">CWE-404</a></td>
<td>Always close resources explicitly and ensure proper cleanup even if an error occurs.</td>
<td>Improper resource shutdown or release happens when a program allocates a resource, such as a file, socket, or database connection, and fails to release it when finished. Unlike normal objects (like numbers or strings), these resources are tied to the operating system and are not freed automatically by garbage collection. If left open, they can pile up and cause memory leaks, file handle exhaustion, or stalled network connections.</td>
</tr>

<tr>
<td><a href=07_concurrency/pyscg-0054/README.md>pyscg-0054</a></td>
<td>Race Condition Within a Thread</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/366.html">CWE-366</a></td>
<td>In multithreaded programming, use synchronization mechanisms, such as locks, to avoid race conditions, which occur when multiple threads access shared resources simultaneously and lead to unpredictable results.</td>
<td></td>
</tr>

<tr>
<th colspan="6" style="text-align: left; padding: 10px;">
<h3 style="margin: 0;">08 Coding Standards</h3>
</th>
</tr>

<tr>
<td><a href=08_coding_standards/pyscg-0031/README.md>pyscg-0031</a></td>
<td>Loop Condition Value Update Within the Loop</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/1095.html">CWE-1095</a></td>
<td>Promote predictable and secure <code>for</code> loops by iterating over a copy or new collection item as described in 4.2 <code>for</code> Statements <a href="https://docs.python.org/3.9/tutorial/controlflow.html#for-statements">Python 3.9 2024</a>.</td>
<td>In-place modification of mutable types such as <code>list</code>, <code>dict</code>, or <code>set</code> that are part of a for loop can result in unpredictable outcomes.</td>
</tr>

<tr>
<td><a href=08_coding_standards/pyscg-0032/README.md>pyscg-0032</a></td>
<td>Use of Same Variable for Multiple Purposes</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/1109.html">CWE-1109</a></td>
<td>Avoid reusing names of variables, functions, classes, built-in functions, packages, or standard Python modules</td>
<td>Redefining identifiers from <em>The Python Standard Library</em> <a href="https://docs.python.org/3/library/index.html">[Python 2025]</a>, any internals <code>str</code> and <code>os</code> or other parts of the project can result in unexpected behavior and errors. Issues can multiply when identifiers are made global in a project.</td>
</tr>

<tr>
<td><a href=08_coding_standards/pyscg-0033/README.md>pyscg-0033</a></td>
<td>Comparison of Object References Instead of Object Contents</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/595.html">CWE-595</a></td>
<td>Prevent unexpected results by knowing the differences between comparison operators such as <code>==</code> and <code>is</code>.</td>
<td>In Python, the <code>==</code> operator is implemented by the <code>__eq__</code> method on an object <a href="https://docs.python.org/3/reference/datamodel.html?highlight=__eq__#object.__eq__">[python.org data model 2023]</a>. For built-in types like <code>int</code> and <code>str</code>, the comparison is implemented in the interpreter. The main issue comes when implementing custom classes, where the default implementation compares object references using the <code>is</code> operator. The <code>is</code> operator compares the identities of the objects, equivalent to <code>id(obj1) == id(obj2)</code>.</td>
</tr>

<tr>
<td><a href=08_coding_standards/pyscg-0034/README.md>pyscg-0034</a></td>
<td>NULL Pointer Dereference</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/476.html">CWE-476</a></td>
<td>Avoiding NULL Pointer Dereference is crucial for preventing runtime errors, and ensuring that your code executes successfully.</td>
<td>* Ensure that you have a valid object before callings its instance methods.</td>
</tr>

<tr>
<td><a href=08_coding_standards/pyscg-0035/README.md>pyscg-0035</a></td>
<td>Incomplete Cleanup</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/459.html">CWE-459</a></td>
<td>Leftover temporary files not properly cleaned up after the completion of any script, can lead to resource exhaustion and disable a service.</td>
<td>Temporary files can be used to store data, either between processes, or to preserve memory. Using temporary files comes with several challenges, we need to ensure that the temporary files are removed before the termination of the process. In the case of the process terminating abnormally, we can't rely on a finally block as it could fail to run. In the case that the program still fails to free up the execution, we need to ensure that the temporary files are created with the correct permissions and in the correct location so the OS can cleanup after the process finishes, while ensuring to restrict access to other processes.</td>
</tr>

<tr>
<td><a href=08_coding_standards/pyscg-0036/README.md>pyscg-0036</a></td>
<td>Unchecked Return Value</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/252.html">CWE-252</a></td>
<td>Return values of methods and functions should always be checked to ensure operations have been performed correctly.</td>
<td>When immutable objects are used, methods that aim to modify them have to create a new object with the desired changed and return it. For the results of such methods to take place, the developer must remember to assign the new value to a variable, otherwise it won't be accessible. They can also be used to handle unexpected behaviors by returning specific values (such as <code>None</code> or a other default values) that may require additional safety checks.</td>
</tr>

<tr>
<td><a href=08_coding_standards/pyscg-0037/README.md>pyscg-0037</a></td>
<td>Reachable Assertion</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/617.html">CWE-617</a></td>
<td>Assertions are a useful developer tool, but they cannot be relied upon to be present in a production environment. Incorrect function arguments should be handled by an appropriate exception.</td>
<td>Python removes assertions when a script is run with the <code>-O</code>  and <code>-OO</code> options <a href="https://docs.python.org/3.9/using/cmdline.html?highlight=pythonoptimize#cmdoption-o">[Python 3.9 Documentation]</a>. The <code>-O</code> options is for optimisation. It removes asserts statements from bytecode, removes docstrings from functions/classes and sets <code>__debug__</code> to False. It is used for slightly faster execution and smaller bytecode files. <code>-OO</code> does everything that <code>-O</code>does but it additionally removes module-level docstrings and creates an even more compact bytecode.</td>
</tr>

<tr>
<th colspan="6" style="text-align: left; padding: 10px;">
<h3 style="margin: 0;">09 Cryptography</h3>
</th>
</tr>

<tr>
<td><a href=09_cryptography/pyscg-0038/README.md>pyscg-0038</a></td>
<td>Use of Insufficiently Random Values</td>
<td></td>
<td><a href="https://cwe.mitre.org/data/definitions/330.html">CWE-330</a></td>
<td>When programming cryptographic functions ensure to use a Pseudo-Random Number Generator (PRNG) source that is random enough to be suitable for encryption.</td>
<td>Certain algorithms can create sequences of numbers that approximate random distributions <a href="https://rules.sonarsource.com/python/RSPEC-2245/">[sonar 2024]</a>. These algorithms, known as pseudorandom number generators (PRNGs) are numbers generated by a computational process and appear random, even though they are produced by a deterministic algorithm. This means that, unlike truly random numbers, which are inherently unpredictable, pseudorandom numbers are generated in a predictable sequence as long as you know the starting point, or the seed, and the algorithm used to generate them.</td>
</tr>

</table>

## Notes

- This table contains all 55 pyscg rules from the Python Secure Coding Guide
- The "New Title" column is left empty for future title revisions
- First sentences and paragraphs are extracted directly from each rule's README.md file
- Rules are organized by sections: Introduction (01), Encoding/Strings (02), Numbers (03), Neutralization (04), Exception Handling (05), Logging (06), Concurrency (07), Coding Standards (08), and Cryptography (09)