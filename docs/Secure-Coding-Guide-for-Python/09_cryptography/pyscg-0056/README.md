# pyscg-0056: Assure to use and verify Signed Software

Verify a downloaded artifact against a digest or signature obtained through a separate channel before executing it.

Transport security, used for downloading an artifact such as a Python installer or .whl wheel file, verifies the authenticity of the host we download from and not the authetnicity of the artefact it self. Now a mirror, a caching proxy, a compromised build host, or anyone able to alter the response body can substitute code including the SHA that would be used to verify integrity.

So we need a trustworthy alternative transport channel to allowing integrity verification.

A SHA only becomes usefull if we can verify that its correct if we can query an authority via a trusted independent channel.

Software or artifacts can be downloaded and installed either through a package manager or without.

As of writing this rule, the following package managers enforce both integrity and authenticity verification by default:

- `apt` (Debian, Ubuntu)
- `dnf` / `yum` (Red Hat, Fedora, CentOS)
- `zypper` (SUSE, openSUSE)
- `pacman` (Arch Linux)
- `apk` (Alpine)
- `nix` (NixOS)
- App Store (macOS, iOS)
- Microsoft Store (Windows)
- Google Play (Android)
- F-Droid (Android)

Others either:

- Do not enforce verification
- Only cover integrity checks without proving publisher identity

Installing `.exe`, `.rpm` or `.whl` artefacts directly without without a packaage manager, is typically missing security checks!



Signed software allows integrity and authenticity verification at scale with zero need to trust anyone in between the creator of an artefact, such as CPython it self or a `.whl` wheel file and consumer installing it.

Data from [OSV.dev](https://osv.de) shows the scale malware code attacks that exists entirely outside CVE tracking

*Malware and CVEs by year on Python based projects*

| Year | Malware (`MAL-`) | CVEs | Malware with a CVE | Malware share |
| :----- | -----------------: | -----: | -------------------: | --------------: |
| 2023 | 6,468\* | 497 | 0 | 93%\* |
| 2024 | 2,478 | 793 | 0 | 76% |
| 2025 | 1,419 | 721 | 0 | 66% |

This creates a visibility gap: the OSV MAL database tracks thousands of malicious PyPI packages per year that have no CVE, no CVSS score, and no EPSS rating.

>NOTE: Zero trust principal also requires artefacts to be free of secrets.


## Code Examples

The following examples demonstrate how to inspect the signature verification your OS already performed when installing Python.

### Linux (Debian/Ubuntu)

[*example01.sh:*](example01.sh)

```bash
#!/bin/bash
# SPDX-FileCopyrightText: OpenSSF project contributors
# SPDX-License-Identifier: MIT
# example01.sh — Verify the installed python3 package signature (Debian/Ubuntu)
set -euo pipefail

# Which package owns the python3 binary?
PKG=$(dpkg -S "$(which python3)" | cut -d: -f1)

# Verify its installed files against the signed package metadata
dpkg --verify "$PKG"

# Show the repo GPG key that authenticated the package
apt-key adv --list-public-keys --keyid-format long 2>/dev/null | grep -A1 "^pub"
```

### Windows

[*example01.ps1:*](example01.ps1)

```powershell
# SPDX-FileCopyrightText: OpenSSF project contributors
# SPDX-License-Identifier: MIT
# example01.ps1 — Verify the installed python3 binary signature (Windows)

$python = (Get-Command python).Source
Get-AuthenticodeSignature $python
```

The mobile platforms (iOS, Android) are the strongest model: verification is enforced at the OS level and cannot be bypassed without rooting/jailbreaking the device.
