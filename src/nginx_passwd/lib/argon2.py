# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2022-present Gene C <arch@sapience.com>

"""
argon2-cffi
See https://argon2-cffi.readthedocs.io/en/stable/api.html
"""
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from argon2.exceptions import VerificationError
from argon2.exceptions import InvalidHashError


def argon2_password_hash(passwd: str) -> str:
    """
    Generate argpon2 password hash
    """
    ph = PasswordHasher()
    phash = ph.hash(passwd)
    return phash


def argon2_verify_password(phash: str, passwd: str) -> bool:
    """
    Verify password hash
    """
    ph = PasswordHasher()
    verify: bool = False
    try:
        verify = ph.verify(phash, passwd)
    except (VerifyMismatchError, VerificationError, InvalidHashError):
        verify = False

    return verify
