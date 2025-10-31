# Secure Coding One Stop Shop for Python

> ⓘ  NOTE: This is a draft to come up with chapters as per #894
> The structure of  a custom layout
> It only contains the main table and is using html tags
>

Second draft for the [readme_custom.md](readme_custom.md) version. 

Observations from creating the sections:
<table border=1>
<tr>
<th>Section ID</th>
<th>Section</th>
<th># Rules</th>
<th>Comment</th>
</tr>

<tr>
<th>intro</th>
<th>01 Inroduction</th>
<td>3</td>
<td>Seemingly good fit for a start</td>
</tr>

<tr>
<th>enc_str</th>
<th>02 Encoding and Strings</th>
<td>4</td>
<td>Good fit, merge from "input from lesser trusted source" and "strings", some moved to logs</td>
</tr>

<tr>
<th>num</th>
<th>03 Numbers</th>
<td>7</td>
<td>Good fit.</td>
</tr>

<tr>
<th>ntrl</th>
<th>04 Neutralisation</th>
<td>7</td>
<td>Good fit now, better fit then 'strings', slightly overloaded now</td>
</tr>

<tr>
<th>exc</th>
<th>05 Exceptions</th>
<td>5</td>
<td>Good fit now, better fit then 'strings', slightly overloaded now</td>
</tr>

<tr>
<th>log</th>
<th>06 Logging</th>
<td>4</td>
<td>Good fit now, better fit then 'strings', slightly overloaded now</td>
</tr>

<tr>
<th>srl_dsrl</th>
<th>07 Serialization Deserialization</th>
<td>1</td>
<td>Good fit, but only one rule</td>
</tr>

<tr>
<th>conc</th>
<th>08 Concurrency</th>
<td>7</td>
<td>Good fit</td>
</tr>

<tr>
<th>cod_std</th>
<th>09 Coding Standards</th>
<td>7</th>
<td>Reasonable fit, rules moved from MISC</td>
</tr>

<tr>
<th>crypt</th>
<th>10 Cryptography</th>
<td>01</td>
<td>Good fit, only one rule atm but expected to be used to discuss the missing subject</td>
</tr>

</table>

<br><hr><br>

<table border=1>
  <colgroup><col style="width:800px;"><col style="width:240px;"></colgroup>
<tr>
<th>01 Introduction</th>
<th>Prominent CVEs</th>
</tr>

<tr>
<td><a href="CWE-664/CWE-501/README.md">pyscg-intro-0501: Trust Boundary Violation</a></td>
<td><a href="https://www.cvedetails.com/cve/CVE-2023-28597">CVE-2023-28597</a>, CVSSv3.0: <b style='color:orange'>7.5</b>,<br>EPSS: <b>00.11</b> (05.11.2024)</td>
</tr>

<tr><td><a href="CWE-693/CWE-798/README.md">pyscg-intro-0798: Use of hardcoded credentials</a></td><td></td></tr>
<tr><td><a href="CWE-691/CWE-783/README.md">pyscg-intro-0783: Operator Precedence Logic Error</a></td><td></td></tr>

<tr>
<th>02 Encoding and Strings</th>
<th>Prominent CVEs</th>
</tr>
<tr><td><a href="CWE-707/CWE-175/README.md">pyscg-enc_str-0175: Improper Handling of Mixed Encoding</a></td><td></td></tr>

<tr>
<td><a href="CWE-707/CWE-180/README.md">pyscg-enc_str-0180: Incorrect behavior order: Validate before Canonicalize</a></td>
<td><a href="https://www.cvedetails.com/cve/CVE-2022-26136/">CVE-2022-26136</a>,<br>CVSSv3.1: <b style='color:red'>9.8</b>, <br>EPSS: <b>00.28</b> (31.12.20255)</td>
</tr>

<tr><td><a href="CWE-693/CWE-182/README.md">pyscg-enc_str-0182: Enforce control over encoding such as UTF-8</a></td></tr>

<tr><td><a href="CWE-707/CWE-838/README.md">pyscg-enc_str-0838: Inappropriate Encoding for Output Context</a></td><td></td></tr>

<tr><th>03 Numbers</th><th>Prominent CVEs</th></tr>
<tr><td><a href="CWE-682/CWE-1339/README.md">pyscg-num-1339: Avoid floating-point and use integers or the decimal module to ensure precision in applications that require high accuracy, such as in financial or banking computations</a></td><td></td></tr>
<tr><td><a href="CWE-682/CWE-191/README.md">pyscg-num-0191: Ensure that integer overflow is properly handled in order to avoid unexpected behavior.</a></td><td></td></tr>
<tr><td><a href="CWE-682/CWE-1335/01/README.md">pyscg-num-1335: Promote readability and compatibility by using mathematical written code with arithmetic operations instead of bit-wise operations</a></td><td></td></tr>
<tr><td><a href="CWE-664/CWE-197/README.md">pyscg-num-0197:Ensure to have predictable outcomes in loops by using int instead of float variables as a counter</a></td><td></td></tr>
<tr><td><a href="CWE-664/CWE-197/01/README.md">pyscg-num-0197-01: Make conscious design decisions on how conversions are rounded</a></td><td></td></tr>
<tr><td><a href="CWE-664/CWE-681/README.md">pyscg-num-0681: String representations of floating-point numbers must not be compared or inspected outside of specialized modules such as decimal or math</a></td><td></td></tr>
<tr><td><a href="CWE-664/CWE-681/01/README.md">pyscg-num-0681-01: Avoid using floating-point literals.</a></td><td></td></tr>

<tr><th>04 Neutralization</th><th>Prominent CVEs</th></tr>
<tr><td><a href="CWE-693/CWE-184/README.md">pyscg-ntrl-0184: Use 'allow lists' to avoid continuesly updates to 'deny lists'.</a></td><td></td></tr>

<tr>
  <td><a href="CWE-664/CWE-134/README.md">pyscg-ntrl-0134: Use of Externally-Controlled Format String</a></td>
  <td><a href="https://www.cvedetails.com/cve/CVE-2022-27177/">CVE-2022-27177</a>,<br/>CVSSv3.1: <strong style='color:darkred'>>9.8</strong>,<br/>EPSS: <strong>00.37</strong> (01.12.2023)</td>
</tr>

<tr>
  <td><a href="CWE-707/CWE-78/README.md">pyscg-ntrl-0078: Improper Neutralization of Special Elements Used in an OS Command ("OS Command Injection")</a></td>
  <td><a href="https://www.cvedetails.com/cve/CVE-2024-43804/">CVE-2024-43804</a>,<br/>CVSSv3.1: <strong>8.8</strong>,<br/>EPSS: <strong>00.06</strong> (08.11.2024)</td>
</tr>

<tr>
 <td><a href="CWE-707/CWE-89/README.md">pyscg-ntrl-0089: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')</a></td>
 <td><a href="https://www.cvedetails.com/cve/CVE-2019-8600">CVE-2019-8600</a>, CVSSv3.1: <b style='color:red'>9.8</b>,<br>EPSS: <b>01.43</b> (18.02.2024)</td>
</tr>

<tr>
<td><a href="CWE-664/CWE-843/README.md">pyscg-ntrl-0843: Access of Resource Using Incompatible Type ('Type Confusion')</a></td>
<td><a href="https://www.cvedetails.com/cve/CVE-2021-29513">CVE-2021-29513</a>, CVSSv3.1: <b style='color:orange'>7.8</b>,<br/>EPSS: <b>00.02</b> (13.05.2025)
</td>
</tr>

<tr>
  <td><a href="CWE-664/CWE-409/README.md">pyscg-ntrl-0409: Improper Handling of Highly Compressed Data (Data Amplification)</a></td>
  <td><a href="https://www.cvedetails.com/cve/CVE-2019-9674/">CVE-2019-9674</a>, CVSSv3.1: <b style='color:orange'>7.5</b>, EPSS <b>1.2%</b>(10.09.2025)</td>
</tr>

<tr>
  <td><a href="CWE-664/CWE-426/README.md">pyscg-ntrl-0426: Untrusted Search Path</a></td>
  <td><a href="https://www.cvedetails.com/cve/CVE-2015-1326">CVE-2015-1326</a>,<br/>CVSSv3.0: <strong style='color:red'>8.8</strong>,<br/>EPSS: <strong>00.20</strong> (23.11.2023)</td>
</tr>

<tr><th>05 Exception handling</th><th>Prominent CVEs</th></tr>
<tr><td><a href="CWE-703/CWE-397/README.md">pyscg-exc-0397: Declaration of Throws for Generic Exception</a></td><td></td></tr>
<tr><td><a href="CWE-703/CWE-755/README.md">pyscg-exc-0755: Improper Handling of Exceptional Conditions</a></td><td><a href="https://www.cvedetails.com/cve/CVE-2024-39560">CVE-2024-39560</a>,CVSSv3.1: <strong style='color:yellow'>6.5</strong>,<br/>EPSS: <strong>0.04</strong> (01.11.2024)</td></tr>
<tr><td><a href="CWE-703/CWE-390/README.md">pyscg-exc-0390: Detection of Error Condition without Action</a></td><td></td></tr>
<tr><td><a href="CWE-703/CWE-230/README.md">pyscg-exc-0230: Improper Handling of Missing Values</a></td><td></td></tr>
<tr><td><a href="CWE-703/CWE-754/README.md">pyscg-exc-0754: Improper Check for Unusual or Exceptional Conditions - float</a></td><td></td></tr>

<tr><th>06 Logging</th><th>Prominent CVEs</th></tr>
<tr>
  <td><a href="CWE-664/CWE-532/README.md">pyscg-log-0532: Insertion of Sensitive Information into Log File</a></td>
  <td><a href="https://www.cvedetails.com/cve/CVE-2023-45585">CVE-2023-45585</a>,<br/>CVSSv3.1: <strong>9.8</strong>,<br/>EPSS: <strong>0.04</strong> (01.11.2024)</td>
</tr>
<tr><td><a href="CWE-693/CWE-778/README.md">pyscg-log-0778: Insufficient Logging</a></td><td></td></tr>
<tr><td><a href="CWE-710/CWE-489/README.md">pyscg-log-0489: Active Debug Code</a></td><td><a href="https://www.cvedetails.com/cve/CVE-2018-14649">CVE-2018-14649</a>, CVSSv3.1: <strong style='color:red'>9.8</strong>, EPSS: <strong>69.64</strong> (12.12.2023)</td></tr>
<tr><td><a href="CWE-707/CWE-117/.">pyscg-log-0117: Improper Output Neutralization for Logs</a></td><td></td></tr>

<tr><th>07 Serialization Deserialization</th><th>Prominent CVEs</th></tr>
<tr><td><a href="CWE-664/CWE-502/.">pyscg-log-0502: Deserialization of Untrusted Data</a></td><td><a href="https://www.cvedetails.com/cve/CVE-2018-8021">CVE-2018-8021</a>, CVSSv3.0: <strong style='color:red'>9.8</strong>,<br/>EPSS: <strong>93.54</strong> (05.11.2024)</td></tr>

<tr><th><a href="Intro_to_multiprocessing_and_multithreading">08 Concurrency</a></th><th>Prominent CVE</th></tr>
<tr><td><a href="CWE-664/CWE-400/README.md">pyscg-conc-0400: Uncontrolled Resource Consumption</a></td><td></td></tr>
<tr><td><a href="CWE-664/CWE-410/README.md">pyscg-conc-0410: Insufficient Resource Pool</a></td><td></td></tr>
<tr><td><a href="CWE-664/CWE-833/README.md">pyscg-conc-0833: Deadlock</a></td><td></td></tr>
<tr><td><a href="CWE-691/CWE-362/README.md">pyscg-conc-0362: Concurrent Execution Using Shared Resource with Improper Synchronization ("Race Condition")</a></td><td></td></tr>
<tr><td><a href="CWE-664/CWE-584/README.md">pyscg-conc-0584: Return Inside Finally Block</a></td><td></td></tr>
<tr><td><a href="CWE-664/CWE-665/README.md">pyscg-conc-0665: Improper Initialization</a></td><td></td></tr>
<tr><td><a href="CWE-703/CWE-392/README.md">pyscg-conc-0392: Missing Report of Error Condition in a Threadpool</a></td><td></td></tr>

<tr><th>08 Coding Standards</th><th>Prominent CVE</th></tr>
<tr><td><a href="CWE-710/CWE-1095/README.md">pyscg-cod_std-1095: Loop Condition Value Update within the Loop</a></td><td></td></tr>
<tr><td><a href="CWE-710/CWE-1109/README.md">pyscg-cod_std-1109: Use of Same Variable for Multiple Purposes</a></td><td></td></tr>
<tr><td><a href="CWE-697/CWE-595/README.md">pyscg-cod_std-0595: Comparison of Object References Instead of Object Contents</a></td><td></td></tr>
<tr><td><a href="CWE-703/CWE-476/README.md">pyscg-cod_std-0476: NULL Pointer Dereference</a></td><td></td></tr>
<tr><td><a href="CWE-664/CWE-459/README.md">pyscg-cod_std-0459: Incomplete Cleanup</a></td><td></td></tr>
<tr><td><a href="CWE-703/CWE-252/README.md">pyscg-cod_std-0252: Unchecked Return Value</a></td><td></td></tr>
<tr><td><a href="CWE-691/CWE-617/README.md">pyscg-cod_std-0617: Reachable Assertion</a></td><td></td></tr>

<tr><th>10 Cryptography</th><th>Prominent CVE</th></tr>
<tr><td><a href="CWE-693/CWE-330/README.md">pyscg-crypt-0330: Use of Insufficiently Random Values</a></td><td><a href="https://www.cvedetails.com/cve/CVE-2020-7548">CVE-2020-7548</a>, CVSSv3.1: <strong style='color:red'>9.8</strong><br>EPSS: <strong>0.22</strong> (12.12.2024)</td></tr>
</table>

## License

* [CC-BY 4.0](../../LICENSES/CC-BY-4.0.txt) for documentation
* [MIT](../../LICENSES/MIT.txt) for code snippets
