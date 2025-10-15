# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2022-present Gene C <arch@sapience.com>
"""
bcrypt
See https://github.com/pyca/bcrypt/
"""
import bcrypt


def bcrypt_password_hash(passwd: str) -> str:
    """
    Generate bcryupt password hash
    """
    if len(passwd) > 72:
        passwd = passwd[:72]
    passwd_bytes = passwd.encode()
    phash_bytes = bcrypt.hashpw(passwd_bytes, bcrypt.gensalt())
    phash = phash_bytes.decode()
    return phash


def bcrypt_verify_password(phash: str, passwd: str) -> bool:
    """
    Verify bcrypt password hash
    """
    if len(passwd) > 72:
        passwd = passwd[:72]
    passwd_bytes = passwd.encode()
    phash_bytes = phash.encode()
    try:
        verify = bcrypt.checkpw(passwd_bytes, phash_bytes)
    except ValueError:
        verify = False
    return verify
