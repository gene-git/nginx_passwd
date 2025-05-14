# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2022-present  Gene C <arch@sapience.com>
"""
 Generate password entry
"""
from typing import (List)


def hash_algos_active() -> List[str]:
    """
    list of (currently) active hash functions
    """
    algos = ['argon2', 'pbkdf2_sha512', 'pbkdf2_sha256',
             'sha512', 'sha256', 'bcrypt']
    return algos


def hash_algos_deprecated() -> List[str]:
    """
    list of deprecated but supported hash functions
    """
    depr = ['apr_md5', 'apr1', 'md5']
    return depr


def hash_algo_default() -> str:
    """
    default algo to use of not specified
    """
    return 'sha256'
