# comparing different arrangements of the the main sections

Purpose of these drafts is to organize the rules into a continues learning path.
Having similar rules below a section also allows avoiding repetition and filling in generics as we did with the [Intro to Multiprocessing and Multithreading](Intro_to_multiprocessing_and_multithreading/readme.md)
We also want to address the "mixup with MITRE" #805 issue while re-arranging the rules.

## The [Readme based on previous layout](readme_based_on_previous_layout.md) chapters as per #894 before adopting MITRE CWE numbering

Following section have no Python rules:

- OBJ
- SEC
- TSM
- THI

<table border="1" cellpadding="5">
  <tr>
    <th>Category</th>
    <th>Count</th>
  </tr>
  <tr>
    <td>IDS</td>
    <td>4</td>
  </tr>
  <tr>
    <td>DCL</td>
    <td>2</td>
  </tr>
  <tr>
    <td>EXP init and declare</td>
    <td>5</td>
  </tr>
  <tr>
    <td>NUM</td>
    <td>11</td>
  </tr>
  <tr>
    <td>STR</td>
    <td>2</td>
  </tr>
  <tr>
    <td>ERR</td>
    <td>6</td>
  </tr>
  <tr>
    <td>VNA visibility</td>
    <td>2</td>
  </tr>
  <tr>
    <td>TPS Thread pool</td>
    <td>5</td>
  </tr>
  <tr>
    <td>FIO</td>
    <td>2</td>
  </tr>
  <tr>
    <td>SER</td>
    <td>1</td>
  </tr>
  <tr>
    <td>ENV</td>
    <td>3</td>
  </tr>
  <tr>
    <td>MSC misc</td>
    <td>2</td>
  </tr>
  <tr>
    <td>unsorted</td>
    <td>4</td>
  </tr>
</table>

## The [Readme based on learningpython.org](readme_based_on_learnpython-org.md)

<table border=1>
<tr>
<th>Section title</th>
<th># Rules</th>
<th>Comment</th>
</tr>

<tr>
<th>Learn the basics - Hello World</th>
<td>1</td>
<td>Could also be named Introduction</td>
</tr>

<tr>
<th>Input from a lesser trusted source</th>
<td>7</td>
<td>Not an original learnpython org title</td>
</tr>

<tr>
<th>Lists</th>
<td>0</td>
<td>No rules</td>
</tr>

<tr>
<th>Basic Operators</th>
<td>1</td>
<td>To many of these are in other sections</td>
</tr>

<tr>
<th>Advanced - Serialization</th>
<td>1</td>
<td>Good fit but only one rule</td>
</tr>

<tr>
<th>Advanced - Exception Handling</th>
<td>7</th>
<td>Good fit, overlaps with logging</td>
</tr>

<tr>
<th>Advanced - Multiprocessing and Multithreading</th>
<td>7</td>
<td>Good fit, not original title</td>
</tr>

<tr>
<th>Advanced - ??</th>
<td>2</td>
<td>Rules that don't fit</td>
</tr>

<tr>
<th>Advanced - Misc</th>
<td>6</td>
<td>Should not exist.</td>
</tr>
</table>

## Current [readme.md](readme.md) based on Pillars

<table border=1>
<tr>
<th>Section title</th>
<th># Rules</th>
<th>Comment</th>
</tr>

<tr>
<th>CWE-664: Improper Control of a Resource Through its Lifetime</th>
<td>20</td>
<td>A lot in one section. Bleeding into multithreading, number and Error handling</td>
</tr>

<tr>
<th>CWE-682: Incorrect Calculation</th>
<td>4</td>
<td>Some precision rules are in CWE-664</td>
</tr>

<tr>
<th>CWE-691: Insufficient Control Flow Management</th>
<td>3</td>
<td>Overlaps into multiprocessing/threading</td>
</tr>

<tr>
<th>CWE-693: Protection Mechanism Failure</th>
<td>6</td>
<td>Good fit</td>
</tr>

<tr>
<th>CWE-697: Incorrect Comparison</th>
<td>1</td>
<td>Good fit but only one rule</td>
</tr>

<tr>
<th>CWE-703: Improper Check or Handling of Exceptional Conditions</th>
<td>8</th>
<td>Reasonable fit, bleeds into numbers and error handling</td>
</tr>

<tr>
<th>CWE-707: Improper Neutralization</th>
<td>6</td>
<td>Good fit</td>
</tr>

<tr>
<th>CWE-710: Improper Adherence to Coding Standards</th>
<td>3</td>
<td>Good fit with several rules</td>
</tr>

<tr>
<th>Multiprocessing and Multithreading</th>
<td>6</td>
<td>Good fit, not a Pillar. Shares content with several pillars</td>
</tr>
</table>

## The [readme_custom.md](readme_custom.md) first draft of self baked sections

<table border=1>
<tr>
<th>Section title</th>
<th># Rules</th>
<th>Comment</th>
</tr>

<tr>
<th>Learn the basics</th>
<td>2</td>
<td>Could also be called 'introduction', appears a good choice for setting the scene</td>
</tr>

<tr>
<th>Input from a lesser trusted source</th>
<td>6</td>
<td>Bleeds into 'strings' section, hard to figure out what to put into it</td>
</tr>

<tr>
<th>Output to a lesser trusted source</th>
<td>1</td>
<td>Tricky as it also bleeds into 'strings' making it hard to figure out what to put in it</td>
</tr>

<tr>
<th>Strings</th>
<td>3</td>
<td>Bad fit. Listed rules use input output in its examples to explain encoding issues. CWE-184 'allowed lists' is only here as its using encoding in its example's.</td>
</tr>

<tr>
<th>Numbers (6 rules)</th>
<td>6</td>
<td>Good fit.</td>
</tr>

<tr>
<th>Basic Operators</th>
<td>1</th>
<td>Bad fit as we only have one rule in here</td>
</tr>

<tr>
<th>Serialization Deserialization</th>
<td>1</td>
<td>Good fit but only one rule</td>
</tr>

<tr>
<th>Exception Handling</th>
<td>6</td>
<td>Good fit with several rules</td>
</tr>

<tr>
<th>Multiprocessing and Multithreading</th>
<td>6</td>
<td>Good fit with several rules</td>
</tr>

<tr>
<th>Cryptography</th>
<td>1</td>
<td>Good fit, only one rule atm but expected to be used to discuss the missing subject</td>
</tr>

<tr>
<th>Misc</th>
<td>11</td>
<td>Contains 11 or 1/4 of the rules. Indicating missing sections</td>
</tr>
</table>

## The [readme_custom_v2.md](readme_custom_v2.md) self baked sections

<table border=1>
<tr>
<th>Section</th>
<th># Rules</th>
<th>Comment</th>
</tr>

<tr>
<th>Inroduction</th>
<td>2</td>
<td>Seemingly good fit for a start</td>
</tr>

<tr>
<th>Encoding and Strings</th>
<td>2</td>
<td>Reasonable fit, merge from "input from lesser trusted source" and "strings", some moved to logs</td>
</tr>

<tr>
<th>Numbers</th>
<td>7</td>
<td>Good fit.</td>
</tr>

<tr>
<th>Exception handling and logging</th>
<td>13</td>
<td>Good fit now, better fit then 'strings', slightly overloaded now</td>
</tr>

<tr>
<th>Serialization Deserialization</th>
<td>1</td>
<td>Good fit, but only one rule</td>
</tr>

<tr>
<th>Multiprocessing and Multithreading</th>
<td>6</td>
<td>Good fit</td>
</tr>

<tr>
<th>Improper Adherence to Coding Standards</th>
<td>8</th>
<td>Reasonable fit, rules moved from MISC</td>
</tr>

<tr>
<th>Cryptography</th>
<td>1</td>
<td>Good fit, only one rule atm but expected to be used to discuss the missing subject</td>
</tr>

</table>
