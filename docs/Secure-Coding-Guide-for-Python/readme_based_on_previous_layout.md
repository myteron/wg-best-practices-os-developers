# Secure Coding One Stop Shop for Python

> ⓘ  NOTE: This is a draft to come up with chapters as per #894
> The structure in this readme is based on what we had before adopting MITRE CWE numbering
> It only contains the main table.

|Input from a lesser trusted source|Prominent CVE|
|:-----------------------------------------------------------------------------------------------------------------------------------------------|:----|
|[CWE-409: Improper Handling of Highly Compressed Data (Data Amplification)](CWE-664/CWE-409/README.md)||
|[CWE-134: Use of Externally-Controlled Format String](CWE-664/CWE-134/README.md)|[CVE-2022-27177](https://www.cvedetails.com/cve/CVE-2022-27177/),<br/>CVSSv3.1: __9.8__,<br/>EPSS: __00.37__ (01.12.2023)|
|[CWE-184: Incomplete List of Disallowed Input](CWE-693/CWE-184/README.md)||
|[CWE-78: Improper Neutralization of Special Elements Used in an OS Command ("OS Command Injection")](CWE-707/CWE-78/README.md)|[CVE-2024-43804](https://www.cvedetails.com/cve/CVE-2024-43804/),<br/>CVSSv3.1: __8.8__,<br/>EPSS: __00.06__ (08.11.2024)|
|[CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')](CWE-707/CWE-89/README.md)|[CVE-2019-8600](https://www.cvedetails.com/cve/CVE-2019-8600/),<br/>CVSSv3.1: __9.8__,<br/>EPSS: __01.43__ (18.02.2024)|
|[CWE-180: Incorrect behavior order: Validate before Canonicalize](CWE-707/CWE-180/README.md)|[CVE-2022-26136](https://www.cvedetails.com/cve/CVE-2022-26136/),<br/>CVSSv3.1: __9.8__,<br/>EPSS: __00.18__ (24.04.2025)|

|Output to a lesser trusted source|Prominent CVE|
|:-----------------------------------------------------------------------------------------------------------------------------------------------|:----|
|[CWE-117: Improper Output Neutralization for Logs](CWE-707/CWE-117/.)||
|[CWE-838: Inappropriate Encoding for Output Context](CWE-707/CWE-838/README.md)||

|Numbers|Prominent CVE|
|:-----------------------------------------------------------------------------------------------------------------------------------------------|:----|
|[CWE-843: Access of Resource Using Incompatible Type ('Type Confusion')](CWE-664/CWE-843/README.md)|[CVE-2021-29513](https://www.cvedetails.com/cve/CVE-2021-29513),<br/>CVSSv3.1: __7.8__,<br/>EPSS: __00.02__ (13.05.2025)|
|[CWE-681: Incorrect Conversion between Numeric Types](CWE-664/CWE-681/README.md)||
|[CWE-681: Avoid an uncontrolled loss of precision when passing floating-point literals to a Decimal constructor.](CWE-664/CWE-681/01/README.md)||
|[CWE-197: Numeric Truncation Error](CWE-664/CWE-197/README.md)||
|[CWE-197: Control rounding when converting to less precise numbers](CWE-664/CWE-197/01/README.md)||
|[CWE-191: Integer Underflow (Wrap or Wraparound)](CWE-682/CWE-191/README.md)||
|[CWE-1335: Incorrect Bitwise Shift of Integer](CWE-682/CWE-1335/README.md)||
|[CWE-1335: Promote readability and compatibility by using mathematical written code with arithmetic operations instead of bit-wise operations](CWE-682/CWE-1335/01/README.md)||
|[CWE-1339: Insufficient Precision or Accuracy of a Real Number](CWE-682/CWE-1339/.)                            ||
|[CWE-682: Incorrect Calculation](https://cwe.mitre.org/data/definitions/682.html)|Prominent CVE|
|[CWE-230: Improper Handling of Missing Values](CWE-703/CWE-230/.)||

|Life cycle|Prominent CVE|
|:-----------------------------------------------------------------------------------------------------------------------------------------------|:----|
|[CWE-400: Uncontrolled Resource Consumption](CWE-664/CWE-400/README.md)||
|[CWE-252: Unchecked Return Value](CWE-703/CWE-252/README.md)||

|Error handling and exceptions|Prominent CVE|
|:-----------------------------------------------------------------------------------------------------------------------------------------------|:----|
|[CWE-209: Generation of Error Message Containing Sensitive Information](CWE-664/CWE-209/README.md)|[CVE-2013-0773](https://www.cvedetails.com/cve/CVE-2013-0773/),<br/>CVSSv3.1:__3.3__,<br/>EPSS: __00.95__ (23.11.2023)|
|[CWE-532: Insertion of Sensitive Information into Log File](CWE-664/CWE-532/README.md)|[CVE-2023-45585](https://www.cvedetails.com/cve/CVE-2023-45585),<br/>CVSSv3.1: __9.8__,<br/>EPSS: __0.04__ (01.11.2024)|
|[CWE-693: Protection Mechanism Failure](https://cwe.mitre.org/data/definitions/693.html)|Prominent CVE|
|[CWE-754: Improper Check for Unusual or Exceptional Conditions - float](CWE-703/CWE-754/README.md)||
|[CWE-755: Improper Handling of Exceptional Conditions](CWE-703/CWE-755/README.md)|[CVE-2024-39560](https://www.cvedetails.com/cve/CVE-2024-39560),<br/>CVSSv3.1: __6.5__,<br/>EPSS: __0.04__ (01.11.2024)|
|[CWE-392: Missing Report of Error Condition](CWE-703/CWE-392/README.md)||
|[CWE-390: Detection of Error Condition without Action](CWE-703/CWE-390/README.md)||
|[CWE-397: Declaration of Throws for Generic Exception](CWE-703/CWE-397/README.md)||
|[CWE-476: NULL Pointer Dereference](CWE-703/CWE-476/README.md)||

|Serialisation and Deserialization|Prominent CVEs|
|:-----------------------------------------------------------------------------------------------------------------------------------------------|:----|
|[CWE-502: Deserialization of Untrusted Data)](CWE-664/CWE-502/.)|[CVE-2018-8021](https://www.cvedetails.com/cve/CVE-2018-8021),<br/>CVSSv3.0: __9.8__,<br/>EPSS: __93.54__ (05.11.2024)|

|Environment|Prominent CVEs|
|:-----------------------------------------------------------------------------------------------------------------------------------------------|:----|
|[CWE-501: Trust Boundary Violation)](CWE-664/CWE-501/README.md)|[CVE-2023-28597](https://www.cvedetails.com/cve/CVE-2023-28597),<br/>CVSSv3.0: __7.5__,<br/>EPSS: __00.11__ (05.11.2024)|
|[CWE-489: Active Debug Code](CWE-710/CWE-489/README.md)|[CVE-2018-14649](https://www.cvedetails.com/cve/CVE-2018-14649),<br/>CVSSv3.1: __9.8__,<br/>EPSS: __69.64__ (12.12.2023)|

|Multiprocessing and Multithreading|Prominent CVEs|
|:-----------------------------------------------------------------------------------------------------------------------------------------------|:----|
|[CWE-410: Insufficient Resource Pool](CWE-664/CWE-410/README.md)||
|[CWE-459: Incomplete Cleanup](CWE-664/CWE-459/README.md)||
|[CWE-584: Return Inside Finally Block](CWE-664/CWE-584/README.md)||
|[CWE-833: Deadlock](CWE-664/CWE-833/README.md)||
|[CWE-362: Concurrent Execution Using Shared Resource with Improper Synchronization ("Race Condition")](CWE-691/CWE-362/README.md)||

|Misc|Prominent CVEs|
|:-----------------------------------------------------------------------------------------------------------------------------------------------|:----|
|[CWE-426: Untrusted Search Path](CWE-664/CWE-426/README.md)|[CVE-2015-1326](https://www.cvedetails.com/cve/CVE-2015-1326),<br/>CVSSv3.0: __8.8__,<br/>EPSS: __00.20__ (23.11.2023)|
|[CWE-330: Use of Insufficiently Random Values](CWE-693/CWE-330/README.md)|[CVE-2020-7548](https://www.cvedetails.com/cve/CVE-2020-7548),<br/>CVSSv3.1: __9.8__,<br/>EPSS: __0.22__ (12.12.2024)|
|[CWE-665: Improper Initialization](CWE-664/CWE-665/README.md)||
|[CWE-182: Collapse of Data into Unsafe Value](CWE-693/CWE-182/README.md)||
|[CWE-778: Insufficient Logging](CWE-693/CWE-778/README.md)||
|[CWE-617: Reachable Assertion](CWE-691/CWE-617/README.md)||
|[CWE-798: Use of hardcoded credentials](CWE-693/CWE-798/README.md)||
|[CWE-175: Improper Handling of Mixed Encoding](CWE-707/CWE-175/README.md)||
|[CWE-1109: Use of Same Variable for Multiple Purposes](CWE-710/CWE-1109/README.md)||
|[CWE-595: Comparison of Object References Instead of Object Contents](CWE-697/CWE-595/README.md)||
|[CWE-1095: Loop Condition Value Update within the Loop](CWE-710/CWE-1095/README.md)||


## License

* [CC-BY 4.0](../../LICENSES/CC-BY-4.0.txt) for documentation
* [MIT](../../LICENSES/MIT.txt) for code snippets
