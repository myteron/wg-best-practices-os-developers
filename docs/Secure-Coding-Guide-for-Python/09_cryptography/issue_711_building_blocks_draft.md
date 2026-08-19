# Suggested Building blocks for rules in 09 Cryptography:

## What qualifies as a rule in pySCG

- Official Python documentation warning about insecure design patterns.
- Python code fixes triggered by a reported CVE that are not a bug in CPython or its standard library.
- Bugs outside of CPython or the standard library that have no CVE but are a clear violation of recommended design patterns in docs.python.org for CPython >= 3.9.

### What qualifies CVE's to be quoted as a Prominent CVE

- Quote up to two qualifying CVEs per rule.
- Select the CVE with the highest available CVSS version.
- Select the CVE with the highest current EPSS.
- If both selections point to the same CVE, one CVE is sufficient unless a second CVE teaches something materially different.

<table>
  <thead>
    <tr>
      <th>Building block / rule</th>
      <th>Prominent CVEs / Warnings</th>
      <th>MITRE</th>
      <th>Stdlib? + Refs</th>
    </tr>
  </thead>
  <tbody>
    <!-- 09 Cryptography - Introduction -->
    <tr>
      <td>
        <strong>09 Cryptography - Introduction</strong><br>
        Introduces the security goals and mental model for the section:
        confidentiality, integrity, authenticity, trust anchoring, safe
        composition, and why the rules build from primitives toward signed
        software and provenance.
      </td>
      <td></td>
      <td></td>
      <td>
        No<br><br>
        <ul>
          <li><a href="https://www.youtube.com/watch?v=bImuwuGidS0">If It Ain't Broken, Do Fix It</a></li>
          <li><a href="https://opensource.net/security-cryptography-algorithms-python/">Security and Cryptography Algorithms in Python</a></li>
        </ul>
      </td>
    </tr>
    <!-- pyscg-0038 -->
    <tr>
      <td>
        <strong><a href="pyscg-0038/">pyscg-0038: Use Sufficiently Random Values</a></strong><br>
        Cryptographically secure randomness for tokens, nonces, and secret
        material
      </td>
      <td>
        <a href="https://www.cvedetails.com/cve/CVE-2020-7548">CVE-2020-7548</a>,<br>
        CVSSv3.1: <strong>9.8</strong>,<br>
        EPSS: <strong>0.22</strong> (12.12.2024)<br><br>
        <a href="https://peps.python.org/pep-0506/#rationale">PEP 506 rationale</a>:<br>
        <code>random</code> makes it too easy to make serious security errors
        for passwords, tokens, session keys, and similar secrets
      </td>
      <td>
        <a href="https://cwe.mitre.org/data/definitions/330.html">CWE-330</a>,
        <a href="https://cwe.mitre.org/data/definitions/338.html">CWE-338</a>
      </td>
      <td>
        Yes<br><br>
        <ul>
          <li><a href="https://peps.python.org/pep-0506/">PEP 506</a></li>
          <li><a href="https://docs.python.org/3/library/secrets.html"><code>secrets</code></a></li>
        </ul>
      </td>
    </tr>
    <!-- pyscg-0057 -->
    <tr>
      <td>
        <strong>pyscg-0057: Use Cryptographic Hashes for Integrity Checks</strong><br>
        Digest computation, file integrity checks, and pinned-digest
        verification as a minimal integrity mechanism
      </td>
      <td>
        <a href="https://docs.python.org/3/library/hashlib.html#hash-algorithms">docs.python.org warning</a>:<br>
        Some hash algorithms have known collision weaknesses, including MD5
        and SHA1
      </td>
      <td>
        <a href="https://cwe.mitre.org/data/definitions/353.html">CWE-353</a>,
        <a href="https://cwe.mitre.org/data/definitions/354.html">CWE-354</a>,
        <a href="https://cwe.mitre.org/data/definitions/494.html">CWE-494</a>
      </td>
      <td>
        Yes<br><br>
        <ul>
          <li><a href="https://docs.python.org/3/library/hashlib.html"><code>hashlib</code></a></li>
        </ul>
      </td>
    </tr>
    <!-- pyscg-0058 -->
    <tr>
      <td>
        <strong>pyscg-0058: Compare Security-Critical Values in Constant Time</strong><br>
        Constant-time comparison during verification; this is comparison
        hygiene, not HMAC itself
      </td>
      <td>
        docs.python.org warning:<br>
        Use <a href="https://docs.python.org/3/library/hmac.html#hmac.compare_digest"><code>hmac.compare_digest()</code></a>
        instead of <code>==</code> in verification routines
      </td>
      <td>
        <a href="https://cwe.mitre.org/data/definitions/208.html">CWE-208</a>
      </td>
      <td>
        Yes<br><br>
        <ul>
          <li><a href="https://docs.python.org/3/library/hmac.html"><code>hmac</code></a></li>
        </ul>
      </td>
    </tr>
    <!-- pyscg-0059 -->
    <tr>
      <td>
        <strong><a href=./pyscg-0056/README.md>pyscg-0056: Use Keyed Message Authentication for Shared-Secret Integrity</a></strong><br>
        MAC/HMAC, shared-secret authenticity and integrity, and why this does
        not solve publisher provenance or public software distribution<br><br>
        See <a href="pypi_supply_chain_chart.md">PyPI supply-chain data</a>
        for evidence that CVE tracking alone cannot detect malicious packages
      </td>
      <td>
        <a href="https://www.cve.org/CVERecord?id=CVE-2025-48995">CVE-2025-48995</a>,<br>
        CVSSv3.1: <strong>7.5</strong>,<br>
        EPSS: <strong>0.970</strong><br><br>
        <a href="https://www.cve.org/CVERecord?id=CVE-2026-26717">CVE-2026-26717</a>,<br>
        CVSSv3.1: <strong>9.8</strong>,<br>
        EPSS: <strong>0.974</strong>
      </td>
      <td>
        <a href="https://cwe.mitre.org/data/definitions/345.html">CWE-345</a>,
        <a href="https://cwe.mitre.org/data/definitions/354.html">CWE-354</a>
      </td>
      <td>
        Yes<br><br>
        <ul>
          <li><a href="https://docs.python.org/3/library/hmac.html"><code>hmac</code></a></li>
          <li><a href="https://docs.python.org/3/library/hashlib.html"><code>hashlib</code></a></li>
        </ul>
      </td>
    </tr>
    <!-- pyscg-0060 -->
    <tr>
      <td>
        <strong>pyscg-0060: Derive Keys Securely from Passwords</strong><br>
        PBKDF2 / scrypt, salts, work factors, and deriving keys from passwords
        instead of using raw passwords directly
      </td>
      <td>
        <a href="https://docs.python.org/3/library/hashlib.html#key-derivation">docs.python.org guidance</a>:<br>
        Naive algorithms such as <code>sha1(password)</code> are not resistant
        to brute-force attacks; password hashing should be tunable, slow, and
        salted
      </td>
      <td>
        <a href="https://cwe.mitre.org/data/definitions/916.html">CWE-916</a>,
        <a href="https://cwe.mitre.org/data/definitions/759.html">CWE-759</a>,
        <a href="https://cwe.mitre.org/data/definitions/760.html">CWE-760</a>
      </td>
      <td>
        Yes<br><br>
        <ul>
          <li><a href="https://docs.python.org/3/library/hashlib.html"><code>hashlib</code></a></li>
        </ul>
      </td>
    </tr>
    <!-- pyscg-0061 -->
    <tr>
      <td>
        <strong>pyscg-0061: Use TLS with Certificate Validation on Network Interfaces</strong><br>
        Normal TLS client/server use on application interfaces: CA trust,
        hostname validation, presenting certificates on service interfaces,
        and basic mutual TLS concepts
      </td>
      <td>
        docs.python.org guidance:
        <ul>
          <li><a href="https://docs.python.org/3/library/ssl.html#security-considerations">Security considerations</a></li>
          <li><a href="https://docs.python.org/3/library/ssl.html#best-defaults">Best defaults</a></li>
          <li><a href="https://docs.python.org/3/library/ssl.html#verifying-certificates">Verifying certificates</a></li>
          <li><a href="https://docs.python.org/3/library/ssl.html#ssl.create_default_context"><code>create_default_context()</code></a></li>
        </ul>
      </td>
      <td>
        <a href="https://cwe.mitre.org/data/definitions/295.html">CWE-295</a>,
        <a href="https://cwe.mitre.org/data/definitions/297.html">CWE-297</a>
      </td>
      <td>
        Yes<br><br>
        <ul>
          <li><a href="https://docs.python.org/3/library/ssl.html"><code>ssl</code></a></li>
        </ul>
      </td>
    </tr>
    <!-- pyscg-0062 -->
    <tr>
      <td>
        <strong>pyscg-0062: Use Authenticated Encryption Instead of Ad-Hoc Encryption Plus Integrity</strong><br>
        AEAD and why confidentiality and integrity should be combined in a
        single construction instead of assembled ad hoc
      </td>
      <td></td>
      <td>
        <a href="https://cwe.mitre.org/data/definitions/325.html">CWE-325</a>,
        <a href="https://cwe.mitre.org/data/definitions/353.html">CWE-353</a>
      </td>
      <td>
        No<br><br>
        <ul>
          <li><a href="https://cryptography.io/en/latest/hazmat/primitives/aead/">cryptography AEAD</a></li>
        </ul>
      </td>
    </tr>
    <!-- pyscg-0063 -->
    <tr>
      <td>
        <strong>pyscg-0063: Use Digital Signatures for Publisher-Verifiable Authenticity</strong><br>
        Signatures vs HMAC, public/private key model, and authenticity for
        software distributed to many consumers
      </td>
      <td></td>
      <td>
        <a href="https://cwe.mitre.org/data/definitions/347.html">CWE-347</a>,
        <a href="https://cwe.mitre.org/data/definitions/345.html">CWE-345</a>,
        <a href="https://cwe.mitre.org/data/definitions/494.html">CWE-494</a>
      </td>
      <td>
        No<br><br>
        <ul>
          <li><a href="https://cryptography.io/en/latest/hazmat/primitives/asymmetric/">cryptography asymmetric algorithms</a></li>
        </ul>
      </td>
    </tr>
    <!-- pyscg-0064 -->
    <tr>
      <td>
        <strong>pyscg-0064: Validate X.509 Certificates and Chains Outside TLS Handshakes</strong><br>
        Standalone certificate parsing, certificate-chain inspection, path
        validation, trust anchors, and policy checks outside a live TLS
        handshake
      </td>
      <td></td>
      <td>
        <a href="https://cwe.mitre.org/data/definitions/295.html">CWE-295</a>,
        <a href="https://cwe.mitre.org/data/definitions/296.html">CWE-296</a>
      </td>
      <td>
        No<br><br>
        <ul>
          <li><a href="https://cryptography.io/en/latest/x509/tutorial/">cryptography X.509 tutorial</a></li>
          <li><a href="https://cryptography.io/en/latest/x509/verification/">cryptography X.509 verification</a></li>
        </ul>
      </td>
    </tr>
    <!-- pyscg-0065 -->
    <tr>
      <td>
        <strong><a href="pyscg-0065/README.md">pyscg-0065: Verify Package Provenance and Publisher Identity with Index-Hosted Attestations</a></strong><br>
        PEP 740, PyPI attestations, publisher identity, provenance objects,
        and package-index-level verification of signed software. Includes
        DSSE envelopes, signing certificates, transparency log entries, trust
        roots, and verification policy underlying attestation systems.
      </td>
      <td></td>
      <td>
        <a href="https://cwe.mitre.org/data/definitions/494.html">CWE-494</a>,
        <a href="https://cwe.mitre.org/data/definitions/347.html">CWE-347</a>,
        <a href="https://cwe.mitre.org/data/definitions/345.html">CWE-345</a>,
        <a href="https://cwe.mitre.org/data/definitions/295.html">CWE-295</a>
      </td>
      <td>
        No<br><br>
        <ul>
          <li><a href="https://peps.python.org/pep-0740/">PEP 740</a></li>
          <li><a href="https://docs.pypi.org/attestations/">PyPI attestations docs</a></li>
          <li><a href="https://pypi.org/project/pypi-attestations/"><code>pypi-attestations</code></a></li>
          <li><a href="https://www.sigstore.dev/">Sigstore</a></li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

Notes:

* Prominent CVE / warning cells are intentionally left blank where I could not find a clean example that met the requested filter: a real-world insecure-coding or insecure-usage case in Python/application practice rather than a CPython bug, an obsolete-API example, or a third-party implementation flaw unrelated to the rule.
* Where a rule is directly backed by an official `docs.python.org` security warning, that warning can be listed in the evidence column even when no suitable CVE was selected.
* Several rows still have strong support from official Python or PyPA documentation even when no suitable CVE was selected.
* When multiple CVEs qualify for a rule, quote up to two: the one with the highest available CVSS version and the one with the highest current EPSS. If the same CVE is highest on both measures, a single CVE is sufficient unless a second one adds a materially different lesson.
