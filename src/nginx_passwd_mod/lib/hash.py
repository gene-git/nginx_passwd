# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2022-present Gene C <arch@sapience.com>
"""
 Generate password entry

 NB passlib lacks support/maintenance. We want to avoid it wherever
 possible.

 hashlib provides:
     sha1(), sha224(), sha256(), sha384(), sha512(),
     sha3_224(), sha3_256(), sha3_384(), sha3_512(),
     shake_128(), shake_256(),
     blake2b(), and blake2s().
     md5()
"""
# pylint: disable=too-many-return-statements

# ------------------------------------
# Algos - Notes:
#
# Only use passlib for older algos since it is unmaintained and
# it's bcrypt is broken now.
# There is a fork of passlib which is maintained.
#
# Reduce our reliance on it by diretly using
# - bcrypt: python-bcrypt
# - argon2: python-argon2-cffi (uses C implementation via cffi)
# - pbkdf2_sha512 / pbkdf2_sha256 : python-cryptography pbkdf2_sha512
#

#
# Passlib
#
# - deprecated
from passlib.hash import md5_crypt
from passlib.hash import apr_md5_crypt

# - active
from passlib.hash import sha512_crypt
from passlib.hash import sha256_crypt

# End of passlib

# - active continued
from .bcrypt import (bcrypt_password_hash, bcrypt_verify_password)

# modern
from .pbkdf2 import pbkdf2_sha512_password_hash
from .pbkdf2 import pbkdf2_sha512_verify_password
from .pbkdf2 import pbkdf2_sha256_password_hash
from .pbkdf2 import pbkdf2_sha256_verify_password
from .argon2 import argon2_password_hash
from .argon2 import argon2_verify_password

from .hash_algos import hash_to_ident


def _hash_verify(phash: str, passwd: str) -> bool:
    """
    verify the hash
    Return true if verified.
    """
    if not phash:
        return False
    #
    # Find the right algo and verify
    #
    ident = hash_to_ident(phash)
    match ident:
        case 'argon2':
            return argon2_verify_password(phash, passwd)

        case 'pbkdf2-sha512':
            return pbkdf2_sha512_verify_password(phash, passwd)

        case 'pbkdf2-sha256':
            return pbkdf2_sha256_verify_password(phash, passwd)

        case 'bcrypt':
            return bcrypt_verify_password(phash, passwd)

        case 'sha512':
            return sha512_crypt.verify(passwd, phash)

        case 'sha256':
            return sha256_crypt.verify(passwd, phash)

        case 'md5':
            return md5_crypt.verify(passwd, phash)

        case 'apr_md5' | 'apr1':
            # apr1 backward compat only
            return apr_md5_crypt.verify(passwd, phash)

        case _:
            print('Warning: unknown password hash algorithm')
            if sha256_crypt.identify(phash):
                return sha256_crypt.verify(passwd, phash)
    return False


def generate_password(algo: str, passwd: str) -> str:
    """
    generate password hash item
    """
    phash: str = ''

    match algo:
        case 'argon2':
            phash = argon2_password_hash(passwd)

        case 'pbkdf2_sha512' | 'pbkdf2-sha512':
            phash = pbkdf2_sha512_password_hash(passwd)

        case 'pbkdf2_sha256' | 'pbkdf2-sha256':
            phash = pbkdf2_sha256_password_hash(passwd)

        case 'bcrypt':
            phash = bcrypt_password_hash(passwd)

        case 'sha512':
            phash = sha512_crypt.hash(passwd)

        case 'sha256':
            phash = sha256_crypt.hash(passwd)

        case 'md5':
            phash = md5_crypt.hash(passwd)

        case 'apr_md5' | 'apr1' | 'apr-md5':
            # apr1 backward compat only
            phash = apr_md5_crypt.hash(passwd)

        case _:
            phash = sha256_crypt.hash(passwd)

    return phash


def verify_password(phash: str, passwd: str) -> bool:
    """
    Verify user password from password hash and password
    """
    verify: bool = False
    phash = phash.rstrip()
    verify = _hash_verify(phash, passwd)
    return verify
