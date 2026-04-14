# One Stop Shop 🐍: OpenSSF Releases Secure Coding Guide for Python

By [OpenSSF](https://openssf.org/author/openssf/) · March 2026 · [Blog](https://openssf.org/category/blog/)

---

*By TODO: fill in full list of editors*

Onboarding new developers requires a learning resource that can act as a baseline of knowledge in secure coding that is independent of specific frameworks.

Python is one of the most widely adopted programming languages in the world, powering everything from web applications and data pipelines to AI/ML systems and cloud infrastructure. Yet secure coding resources for Python have historically lagged behind those available for languages like Java, C, and C++. The OpenSSF [Secure Coding Guide for Python](https://best.openssf.org/Secure-Coding-Guide-for-Python/) closes that gap by providing developers with a practical, example-driven resource for writing more secure Python code. The guide covers over 50 rules across 9 sections, each with working code examples that demonstrate both the vulnerability and its mitigation.

## Why We Built This Guide

Comprehensive secure coding standards have long existed for languages like Java ([SEI CERT Oracle Coding Standard for Java](https://wiki.sei.cmu.edu/confluence/display/java/SEI+CERT+Oracle+Coding+Standard+for+Java)), C, and C++. For Python, the available resources were either high-level and language-agnostic, or tied to a single web framework. When onboarding new developers, we needed a baseline of secure coding knowledge that was framework-independent, covered core Python, and could serve as a self-study resource without requiring 40+ hours of training. Nothing like that existed, so we built it ourselves under the OpenSSF Best Practices Working Group.

The result is a guide that focuses on CPython ≥ 3.9 and the standard library, deliberately avoiding dependencies on any specific web framework or third-party module. This keeps the material relevant regardless of which stack a team uses and ensures the secure coding principles transfer across projects.

## Why Python Needs a Secure Coding Guide

Python's accessibility is one of its greatest strengths, but it also means that many developers writing Python code may not have formal training in secure software development. Common pitfalls such as OS command injection, deserialization of untrusted data, improper exception handling, and insufficient logging continue to appear in real-world Python applications and libraries. These are not theoretical risks: the guide references prominent CVEs with CVSS scores reaching 9.8, demonstrating the real-world impact of these vulnerabilities.

Existing secure coding standards from [OWASP](https://owasp.org/www-project-developer-guide/release/) and [MITRE CWE Top 25](https://cwe.mitre.org/top25/index.html) provide essential high-level guidance, but they are language-agnostic. Developers need to understand how these risks manifest specifically in Python and what idiomatic Python mitigations look like. That is exactly what this guide delivers.

### Can code scans save us?

Static analysis tools and AI-assisted code review are valuable, but they cannot catch everything. Many security issues stem from design decisions and coding patterns that automated tools struggle to evaluate, such as improper trust boundary handling, missing input neutralization, or subtle operator precedence errors. The guide's code examples are specifically designed so that `noncompliantXX.py` files can be used to test and train analysis tools, while `compliantXX.py` files demonstrate the targeted fix. This makes the guide useful not only for human learners but also for improving the tools themselves.

## What the Guide Covers

The guide is organized into 9 sections covering the most critical areas of secure Python development:

| Section | Topics | Rules |
|:---|:---|:---:|
| 01 Introduction | Trust boundaries, hardcoded credentials, operator precedence, server-side access control | 4 |
| 02 Encoding and Strings | Locale handling, input canonicalization, consistent encoding | 3 |
| 03 Numbers | Floating-point precision, integer wraparound, numeric truncation, type conversion | 8 |
| 04 Neutralization | Format strings, OS command injection, SQL injection, deserialization, path traversal | 8 |
| 05 Exception Handling | Specific exception types, error propagation, cleanup on exceptions | 5 |
| 06 Logging | Sensitive data in logs, security event logging, log neutralization, error output sanitization | 5 |
| 07 Concurrency | Resource consumption, deadlocks, race conditions, improper initialization | 9 |
| 08 Coding Standards | Mutable iteration, built-in redefinition, value comparison, None checks, assertions | 7 |
| 09 Cryptography | Insufficiently random values | 1 |

Each rule follows a consistent structure: a concise description of the risk, a non-compliant code example showing the vulnerability, a compliant solution demonstrating the fix, automated detection results, and references to related CWE entries and other guidelines. Every rule maps to a specific [MITRE CWE](https://cwe.mitre.org/data/definitions/1000.html) weakness.

### An Evidence-Based Approach to Risk

Many secure coding guides assign risk ratings using numeric scales with labels such as impact=HIGH=4 and probability=LOW=3, which are then multiplied and divided to produce an overall score. We found these approaches too abstract and subjective to be genuinely useful for developers trying to understand real-world risk.

Instead, the guide takes an evidence-based approach. The main overview table pairs each rule with a representative CVE from a real-world product, its CVSS score, and its [EPSS](https://www.first.org/epss/) (Exploit Prediction Scoring System) probability rating. CVSS tells you how severe a vulnerability is if exploited; EPSS tells you how likely it is to be exploited in the wild. Together they give a grounded, data-driven picture of risk that abstract rating matrices cannot provide. This also exposes blind spots: rules with high CVSS but low EPSS may indicate areas where the industry underestimates exploitation likelihood, while high EPSS scores highlight vulnerabilities that attackers actively target.

## Practical, Working Code Examples

What sets this guide apart from other secure coding resources is its emphasis on working code. Every rule includes runnable Python examples targeting CPython ≥ 3.9 that developers can clone and execute locally:

```bash
git clone https://github.com/ossf/wg-best-practices-os-developers.git
cd wg-best-practices-os-developers/docs/Secure-Coding-Guide-for-Python
```

Code examples follow a clear naming convention:

- `noncompliantXX.py` – demonstrates the anti-pattern or vulnerability
- `compliantXX.py` – shows the targeted mitigation
- `exampleXX.py` – illustrates specific behavior for understanding

The non-compliant examples include both the vulnerable code and an exploitation section separated by a clear comment marker, making them suitable for testing security analysis tools. The compliant examples address only the specific risk described, keeping them focused and easy to understand.

### Example: OS Command Injection (pyscg-0009)

Consider a common vulnerability: OS command injection via unsanitized user input passed to `subprocess`. The non-compliant example shows how an attacker can inject arbitrary commands, while the compliant solution demonstrates proper input handling using `shlex` and avoiding `shell=True`. Each example is short, typically around 20 lines, and focuses purely on the security issue at hand.

## Who Is This Guide For?

The guide serves multiple audiences:

- **New developers** – A baseline of secure coding knowledge for self-study while learning Python. It standardizes training on common secure coding practices, freeing up experienced team members.
- **Security researchers** – The overview table listing prominent CVEs with CVSS ratings and EPSS frequency scores helps identify blind spots and understand real-world risk distribution.
- **AI and analysis tools** – The structured code examples are designed for training and testing LLMs, static analyzers, and other automated security tools.
- **Educators** – The open-source CC-BY-4.0 license invites anyone to use the content as part of their own teaching materials.

Documentation is written in academic style to support security researchers while using plain English to cater for an international audience. The entire guide is designed to be completed in well under 40 hours of self-study.

## How to Get Involved

The guide is an active, community-driven project and contributions are welcome. Whether it is fixing a typo, improving readability, adding a new code example, or creating entirely new rules to cover missing material, there are many ways to help.

Explore the guide:
[https://best.openssf.org/Secure-Coding-Guide-for-Python/](https://best.openssf.org/Secure-Coding-Guide-for-Python/)

Contribute on GitHub:
[https://github.com/ossf/wg-best-practices-os-developers/tree/main/docs/Secure-Coding-Guide-for-Python](https://github.com/ossf/wg-best-practices-os-developers/tree/main/docs/Secure-Coding-Guide-for-Python)

Join the community on the OpenSSF [Slack](https://slack.openssf.org/) by searching `/join secure-coding-guide-for-python` in the search bar. You can also participate in the bi-weekly working meetings; see the [meeting notes](https://docs.google.com/document/d/1u1gJMtOz-P5Z71B-vKKigzTbIDIS-bUNgNIcfnW4r-k) for details.

### About the Authors

<table>
<tr>
<td width="120"><img src="helge.jpg" alt="Helge" width="100"></td>
<td>Helge Wehder (myteron) is a Security Principal Master with a background in Operations Support Systems (OSS) for large scale radio networks using Python. Helge enjoys creating embedded systems with his 4 children. Plays Bass guitar on a Sunday session in Flann's Ahlone and Inline hockey</td>
</tr>
<tr>
<td width="120"><img src="thomas.jpg" alt="Thomas" width="100"></td>
<td>Thomas McDermott (tommcd) is a Senior Engineer at Ericsson, where he works as a software engineer with a particular interest in secure coding. He works extensively with Python and Java, with a particular interest in data analysis and Markdown- and notebook-based workflows, and he follows developments in AI-assisted engineering tooling. Before moving into software engineering 14 years ago, Thomas spent earlier parts of his career as a researcher and lecturer in Chemical Engineering and as a design engineer in the energy sector, though a long-standing love of coding (Fortran, C, Python, Mathematica, and Bash since the mid-1990s) eventually won out. He holds a PhD in Chemical Engineering from University College Dublin and an MSc in Applied Software Development, and his research background in molecular simulation and statistical mechanics continues to inform his analytical approach to software engineering and security.</td>
</tr>
<tr>
<td width="120"><img src="hubert.jpg" alt="Hubert" width="100"></td>
<td>Hubert Daniszewski (s19110) is a Java and Python software developer with over five years of experience writing, maintaining, and debugging code in both languages. A former Security Master at TietoEvry, he continues to expand his expertise in secure coding and applies it in practice. He was one of the first contributors to the Secure Coding for Python project, where he reviewed and authored rules, particularly in the area of concurrency.</td>
</tr>
<tr>
<td width="120"><img src="bart.jpg" alt="Bart" width="100"></td>
<td>Bartlomiej Karas (BartKaras1128) is a software engineer and open source contributor with a focus on secure development practices and modern software supply chain resilience. He is actively involved in community-driven initiatives that promote transparency, collaboration, and security across ecosystems. Bartłomiej is particularly interested in automation, CI/CD security, and fostering best practices for developers at all levels.</td>
</tr>
<tr>
<td width="120"><img src="andrew.jpg" alt="Andrew" width="100"></td>
<td>Andrew Costello (andrew-costello) is a Computer Science graduate with a focus on cybersecurity and software engineering. His work centres on practical system design, including machine learning-based malware analysis, and he also works on tools, cars, small engines, and farming, reflecting a strong hands-on engineering mindset. He is particularly interested in building secure, efficient systems that perform reliably in real-world conditions.</td>
</tr>
<tr>
<td width="120"><img src="dean.jpg" alt="Dean" width="100"></td>
<td>Dean Wiley (dwiley258)</td>
</tr>
<tr>
<td width="120"><img src="georg.jpg" alt="Georg" width="100"></td>
<td>Georg Kunz (gkunz) is a passionate advocate for open source software and a long term contributor to a wide range of open source projects and communities. He currently serves on the Technical Advisory Council (TAC) and the Governing Board of the Open Source Security Foundation (OpenSSF), co-chairs the OpenSSF Best Practices Working Group, and is a member of the TODO Group's Steering Committee.</td>
</tr>
<tr>
<td width="120"><img src="noah.jpg" alt="Noah" width="100"></td>
<td>Noah Spahn (noah-de) is an open source software contributor and Associate Professor at Point Loma Nazarene University. He has a broad background in software development and DevSecOps, with experience in applications ranging from Earth science models to data center automation, network forensics and enterprise business solutions.</td>
</tr>
<tr>
<td width="120"><img src="david.jpg" alt="David" width="100"></td>
<td>David Mather (davidmather)</td>
</tr>
</table>
