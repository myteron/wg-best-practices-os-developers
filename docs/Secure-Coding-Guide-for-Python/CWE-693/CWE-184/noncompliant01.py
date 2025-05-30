# SPDX-FileCopyrightText: OpenSSF project contributors
# SPDX-License-Identifier: MIT
"""Compliant Code Example"""

import re
import sys

if sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="UTF-8")


def filter_string(input_string: str):
    """Normalize and validate untrusted string

    Parameters:
        input_string(string): String to validate
    """
    # TODO Canonicalize (normalize) before Validating

    # validate, exclude dangerous tags:
    for tag in re.findall("<[^>]*>", input_string):
        if tag in ["<script>", "<img", "<a href"]:
            raise ValueError("Invalid input tag")


#####################
# attempting to exploit above code example
#####################
names = [
    "YES 毛泽东先生",
    "YES dash-",
    "NOK <script" + "\ufdef" + ">",
    "NOK <script生>",
]
for name in names:
    print(name)
    filter_string(name)
