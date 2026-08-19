# Introduction to Cryptography in Python

This page introduces the security goals and mental model for the cryptography section: confidentiality, integrity, authenticity, trust anchoring, and safe composition. The rules build from primitives toward signed software and provenance.

The following rules are covered in this section:

- [pyscg-0038: Use Sufficiently Random Values](pyscg-0038/README.md)
- pyscg-0057: Use Cryptographic Hashes for Integrity Checks <!-- [issue](link) -->
- pyscg-0058: Compare Security-Critical Values in Constant Time <!-- [issue](link) -->
- [pyscg-0056: Use Keyed Message Authentication for Shared-Secret Integrity](pyscg-0056/README.md) <!-- [issue](link) -->
- pyscg-0060: Derive Keys Securely from Passwords <!-- [issue](link) -->
- pyscg-0061: Use TLS with Certificate Validation on Network Interfaces <!-- [issue](link) -->
- pyscg-0062: Use Authenticated Encryption Instead of Ad-Hoc Encryption Plus Integrity <!-- [issue](link) -->
- pyscg-0063: Use Digital Signatures for Publisher-Verifiable Authenticity <!-- [issue](link) -->
- pyscg-0064: Validate X.509 Certificates and Chains Outside TLS Handshakes <!-- [issue](link) -->
- [pyscg-0065: Verify Package Provenance and Publisher Identity with Index-Hosted Attestations](pyscg-0065/README.md) <!-- [issue](link) -->

## What this section is about

Cryptography in software is not primarily about choosing algorithms. It is about achieving security goals — confidentiality, integrity, and authenticity — through safe composition of well-understood building blocks.

Real systems fail not only because primitives are weak, but because protocols combine otherwise sound pieces badly. A developer does not need to become a cryptographer. They do need to recognize safe patterns, unsafe shortcuts, and where ecosystem tooling must take over.

## Security goals

The rules in this section address five security goals:

- **Confidentiality** — preventing unauthorized access to protected data.
- **Integrity** — detecting unauthorized modification of data.
- **Authenticity** — verifying the identity of the party that produced data.
- **Trust anchoring** — establishing the roots of trust that make verification meaningful.
- **Safe composition** — combining cryptographic operations correctly, because secure primitives assembled carelessly produce insecure systems.

## Why this matters for Python developers

Python's standard library and ecosystem provide accessible cryptographic interfaces. This accessibility is a double-edged sword: it makes good practices easy to adopt but also makes subtle mistakes easy to introduce.

Common pitfalls include:

- Using `random` instead of `secrets` for security-sensitive values.
- Checking integrity with a bare hash but no authenticated channel for the expected digest.
- Encrypting data without integrity protection (no authenticated encryption).
- Reusing keys or nonces across different contexts (lack of domain separation).
- Trusting that a well-known library automatically makes the protocol safe.

## How this section is organized

The rules build from primitives toward signed software and provenance:

1. **Randomness** — the foundation: generating unpredictable values.
2. **Hashes and constant-time comparison** — basic integrity checking and safe verification hygiene.
3. **MACs and key derivation** — shared-secret authentication and turning passwords into keys.
4. **TLS** — the standard mechanism for protecting network communication.
5. **Authenticated encryption** — combining confidentiality and integrity in a single construction.
6. **Digital signatures** — public-key authenticity for software distributed to many consumers.
7. **Certificate validation** — understanding trust chains outside the TLS handshake.
8. **Package attestations and provenance** — verifying signed software at the ecosystem level.

Each rule focuses on a specific building block and teaches when to use it, what it does not guarantee, and how to apply it safely in Python.

## Guiding principles

These principles inform the rules throughout this section:

- **Attacks get better over time.** A construction that only barely survives today may become practically exploitable later. Replace weak or fragile designs early.
- **Integrity matters as much as confidentiality.** If attackers can tamper with protected material, they may learn secrets even without directly decrypting anything.
- **Use authenticated constructions.** Encryption without integrity protection is not enough. AEAD is the modern default.
- **Respect domain separation.** Different protocols, purposes, or message types should use different keys and contexts.
- **Know what a primitive does not guarantee.** Using a well-known primitive is not the same as understanding its security boundaries.
- **Safe libraries do not automatically make the full protocol safe.** Insecure composition at the protocol level can break systems even when individual libraries are reputable.

## Further reading

- [If It Ain't Broken, Do Fix It](https://www.youtube.com/watch?v=bImuwuGidS0) — a talk on why protocol composition fails and why old designs should be retired, not merely patched.
- [Security and Cryptography Algorithms in Python](https://opensource.net/security-cryptography-algorithms-python/) — a survey of the major cryptographic building blocks relevant to Python developers.
