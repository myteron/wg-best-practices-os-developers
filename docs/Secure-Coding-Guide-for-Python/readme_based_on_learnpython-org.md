# Secure Coding One Stop Shop for Python

> ⓘ  NOTE: This is a draft to come up with chapters as per #894
> The structure in this readme is based chapters on <https://www.learnpython.org/>
> It only contains the main table and is using html tags

<table border=1>
  <colgroup><col style="width:800px;"><col style="width:240px;"></colgroup>
<tr>
<th>Learn the basics - Hello World</th>
<th>Prominent CVEs</th>
</tr>
<tr>
<td><a href="CWE-664/CWE-501/README.md">CWE-501: Trust Boundary Violation</a></td>
<td><a href="https://www.cvedetails.com/cve/CVE-2023-28597">CVE-2023-28597</a>, CVSSv3.0: <b style='color:orange'>7.5</b>,<br>EPSS: <b>00.11</b> (05.11.2024)</td>
</tr>
</table>
<br>

<table border=1>
  <colgroup>
    <col style="width:800px;">
    <col style="width:240px;">
  </colgroup>
<tr>
<th>Input from a lesser trusted source</th>
<th>Prominent CVEs</th>
</tr>

<tr>
<td><a href="CWE-664/CWE-197/README.md">CWE-197:Ensure to have predictable outcomes in loops by using int instead of float variables as a counter</a></td>
<td></td>
</tr>
<tr>
<td><a href="CWE-664/CWE-197/01/README.md">CWE-197-01: Make conscious design decisions on how conversions are rounded</a></td>
<td></td>
</tr>
<tr>
<td><a href="CWE-664/CWE-681/README.md">CWE-681: String representations of floating-point numbers must not be compared or inspected outside of specialized modules such as decimal or math</a></td>
<td></td>
</tr>
<tr>
<td><a href="CWE-664/CWE-681/01/README.md">CWE-681-01: Avoid using floating-point literals.</a></td>
<td></td>
</tr>
<tr>
<td><a href="CWE-682/CWE-191/README.md">CWE-191: Ensure that integer overflow is properly handled in order to avoid unexpected behavior.</a></td>
<td></td>
</tr>
<tr>
<td><a href="CWE-682/CWE-1339/README.md">CWE-1339: Avoid floating-point and use integers or the decimal module to ensure precision in applications that require high accuracy, such as in financial or banking computations</a></td>
<td></td>
</tr>
<tr>
<td><a href="CWE-664/CWE-843/README.md">CWE-843: Access of Resource Using Incompatible Type ('Type Confusion')</a></td>
<td><a href="https://www.cvedetails.com/cve/CVE-2021-29513">CVE-2021-29513</a>, CVSSv3.1: <b style='color:orange'>7.8</b>,<br/>EPSS: <b>00.02</b> (13.05.2025)
</td>
</tr>
</table>
<br>

<table border=1>
  <colgroup>
    <col style="width:800px;">
    <col style="width:240px;">
  </colgroup>
<tr>
<th>Lists</th>
<th>Prominent CVEs</th>
</tr>
</table>
<br>
<table border=1>
<colgroup>
<col style="width:800px;">
<col style="width:240px;">
</colgroup>
<tr><th>Basic Operators</th><th>Prominent CVEs</th></tr>
<tbody>
<tr>
<td><a href="CWE-682/CWE-1335/01/README.md">CWE-1335: Promote readability and compatibility by using mathematical written code with arithmetic operations instead of bit-wise operations</a></td>
<td></td>
</tr>
</tbody>
</table>
<br>

<table border=1>
  <colgroup>
    <col style="width:800px;">
    <col style="width:240px;">
  </colgroup>
  <thead>
    <tr><th>Advanced - Serialization</th><th>Prominent CVEs</th></tr>
  </thead>
  <tbody>
    <tr><td><a href="CWE-664/CWE-502/.">CWE-502: Deserialization of Untrusted Data</a></td><td><a href="https://www.cvedetails.com/cve/CVE-2018-8021">CVE-2018-8021</a>, CVSSv3.0: <strong style='color:red'>9.8</strong>,<br/>EPSS: <strong>93.54</strong> (05.11.2024)</td></tr>
  </tbody>
</table>
<br>

<table border=1>
  <colgroup><col style="width:800px;"><col style="width:240px;"></colgroup>
  <thead>
    <tr><th>Advanced - Exception Handling</th><th>Prominent CVE</th></tr>
  </thead>
  <tbody>
    <tr><td><a href="CWE-693/CWE-182/README.md">CWE-182: Collapse of Data into Unsafe Value</a></td><td></td></tr>
    <tr><td><a href="CWE-703/CWE-390/README.md">CWE-390: Detection of Error Condition without Action</a></td><td></td></tr>
    <tr><td><a href="CWE-703/CWE-392/README.md">CWE-392: Missing Report of Error Condition</a></td><td></td></tr>
    <tr><td><a href="CWE-703/CWE-397/README.md">CWE-397: Declaration of Throws for Generic Exception</a></td><td></td></tr>
    <tr><td><a href="CWE-703/CWE-754/README.md">CWE-754: Improper Check for Unusual or Exceptional Conditions - float</a></td><td></td></tr>
    <tr><td><a href="CWE-703/CWE-755/README.md">CWE-755: Improper Handling of Exceptional Conditions</a></td><td><a href="https://www.cvedetails.com/cve/CVE-2024-39560">CVE-2024-39560</a>,CVSSv3.1: <strong style='color:yellow'>6.5</strong>,<br/>EPSS: <strong>0.04</strong> (01.11.2024)</td></tr>
    <tr><td><a href="CWE-707/CWE-117/.">CWE-117: Improper Output Neutralization for Logs</a></td><td></td></tr>
  </tbody>
</table>
<br>

<table border=1>
  <colgroup><col style="width:800px;"><col style="width:240px;"></colgroup>
  <thead>
    <tr><th>Advanced - Multiprocessing and Multithreading</th><th>Prominent CVE</th></tr>
  </thead>
  <tbody>
    <tr><td><a href="CWE-664/CWE-400/README.md">CWE-400: Uncontrolled Resource Consumption</a></td><td></td></tr>
    <tr><td><a href="CWE-664/CWE-410/README.md">CWE-410: Insufficient Resource Pool</a></td><td></td></tr>
    <tr><td><a href="CWE-664/CWE-833/README.md">CWE-833: Deadlock</a></td><td></td></tr>
    <tr><td><a href="CWE-691/CWE-362/README.md">CWE-362: Concurrent Execution Using Shared Resource with Improper Synchronization ("Race Condition")</a></td><td></td></tr>
  </tbody>
</table>
<br>

<table border=1>
  <colgroup><col style="width:800px;"><col style="width:240px;"></colgroup>
  <thead>
    <tr><th>Advanced - ??</th><th>Prominent CVE</th></tr>
  </thead>
  <tbody>
    <tr><td><a href="CWE-693/CWE-330/README.md">CWE-330: Use of Insufficiently Random Values</a></td><td><a href="https://www.cvedetails.com/cve/CVE-2020-7548">CVE-2020-7548</a>, CVSSv3.1: <strong style='color:red'>9.8</strong><br>EPSS: <strong>0.22</strong> (12.12.2024)</td></tr>
    <tr><td><a href="CWE-693/CWE-798/README.md">CWE-798: Use of hardcoded credentials</a></td><td></td></tr>
  </tbody>
</table>
<br>
<table border=1>
  <colgroup><col style="width:800px;"><col style="width:240px;"></colgroup>
  <thead>
    <tr><th>Advanced - Misc</th><th>Prominent CVE</th></tr>
  </thead>
  <tbody>
    <tr><td><a href="CWE-693/CWE-184/README.md">CWE-184: Incomplete List of Disallowed Input</a></td><td></td></tr>
    <tr><td><a href="CWE-693/CWE-778/README.md">CWE-778: Insufficient Logging</a></td><td></td></tr>
    <tr><td><a href="CWE-703/CWE-230/README.md">CWE-230: Improper Handling of Missing Values</a></td><td></td></tr>
    <tr><td><a href="CWE-703/CWE-476/README.md">CWE-476: NULL Pointer Dereference</a></td><td></td></tr>
    <tr><td><a href="CWE-707/CWE-89/README.md">CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')</a></td><td><a href="https://www.cvedetails.com/cve/CVE-2019-8600">CVE-2019-8600</a>, CVSSv3.1: <b style='color:red'>9.8</b>,<br>EPSS: <b>01.43</b> (18.02.2024)</td></tr>
    <tr><td><a href="CWE-710/CWE-489/README.md">CWE-489: Active Debug Code</a></td><td><a href="https://www.cvedetails.com/cve/CVE-2018-14649">CVE-2018-14649</a>, CVSSv3.1: <strong style='color:red'>9.8</strong>, EPSS: <strong>69.64</strong> (12.12.2023)</td></tr>
  </tbody>
</table>

## License

* [CC-BY 4.0](../../LICENSES/CC-BY-4.0.txt) for documentation
* [MIT](../../LICENSES/MIT.txt) for code snippets
