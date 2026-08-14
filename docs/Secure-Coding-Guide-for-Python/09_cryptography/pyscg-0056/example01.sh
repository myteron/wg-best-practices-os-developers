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
