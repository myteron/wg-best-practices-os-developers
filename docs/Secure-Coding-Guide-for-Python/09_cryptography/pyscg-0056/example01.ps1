# SPDX-FileCopyrightText: OpenSSF project contributors
# SPDX-License-Identifier: MIT
# example01.ps1 — Verify the installed python3 binary signature (Windows)

$python = (Get-Command python).Source
Get-AuthenticodeSignature $python
