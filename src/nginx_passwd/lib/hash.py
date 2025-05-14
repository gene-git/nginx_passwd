# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2022-present  Gene C <arch@sapience.com>
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
import getpass
import logging

# ------------------------------------
# Algos
#
# deprecated
#
from passlib.hash import md5_crypt
from passlib.hash import apr_md5_crypt
#
# active
#
from passlib.hash import sha512_crypt
from passlib.hash import sha256_crypt
from passlib.hash import bcrypt
#
# modern
#
from passlib.hash import argon2
from passlib.hash import pbkdf2_sha512
from passlib.hash import pbkdf2_sha256
# ------------------------------------

from .hash_algos import (hash_algos_active, hash_algos_deprecated)
from .hash_algos import (hash_algo_default)
from ._ngp_base import NgpBase

#
# Remove passlib bcrypt warning if user has python-bcrypt loaded.
#
log = logging.getLogger('passlib.handlers.bcrypt')
if log:
    log.setLevel(logging.CRITICAL)

# -------------
# Public
#


def _get_passwd(ngp: NgpBase) -> str:
    """ get clear password """
    if ngp.opts.passwd:
        passwd = ngp.opts.passwd
    else:
        passwd = getpass.getpass()
    return passwd


def _hash_verify(ngp: NgpBase, phash: str) -> bool:
    """
    verify the hash

    Return true if verified.
    """
    if not phash:
        return False

    passwd = _get_passwd(ngp)

    #
    # Find the right algo and verify
    #
    algos = hash_algos_active()
    algos += hash_algos_deprecated()
    for algo in algos:
        match algo:
            case 'argon2':
                if argon2.identify(phash):
                    return argon2.verify(passwd, phash)

            case 'pbkdf2_sha512':
                if pbkdf2_sha512.identify(phash):
                    return pbkdf2_sha512.verify(passwd, phash)

            case 'pbkdf2_sha256':
                if pbkdf2_sha256.identify(phash):
                    return pbkdf2_sha256.verify(passwd, phash)

            case 'bcrypt':
                if bcrypt.identify(phash):
                    return bcrypt.verify(passwd, phash)

            case 'sha512':
                if sha512_crypt.identify(phash):
                    return sha512_crypt.verify(passwd, phash)

            case 'sha256':
                if sha256_crypt.identify(phash):
                    return sha256_crypt.verify(passwd, phash)

            case 'md5':
                if md5_crypt.identify(phash):
                    return md5_crypt.verify(passwd, phash)

            case 'apr_md5' | 'apr1':
                # apr1 backward compat only
                if apr_md5_crypt.identify(phash):
                    return apr_md5_crypt.verify(passwd, phash)
            case _:
                if sha256_crypt.identify(phash):
                    return sha256_crypt.verify(passwd, phash)
    return False


def generate_password(ngp: NgpBase, algo: str = '') -> str:
    """
    generate password hash item
    """
    if not algo:
        algo = hash_algo_default()

    passwd = _get_passwd(ngp)
    phash: str = ''

    match algo:
        case 'argon2':
            phash = argon2.hash(passwd)

        case 'pbkdf2_sha512':
            phash = pbkdf2_sha512.hash(passwd)

        case 'pbkdf2_sha256':
            phash = pbkdf2_sha256.hash(passwd)

        case 'bcrypt':
            phash = bcrypt.hash(passwd)

        case 'sha512':
            phash = sha512_crypt.hash(passwd)

        case 'sha256':
            phash = sha256_crypt.hash(passwd)

        case 'md5':
            phash = md5_crypt.hash(passwd)

        case 'apr_md5' | 'apr1':
            # apr1 backward compat only
            phash = apr_md5_crypt.hash(passwd)

        case _:
            phash = sha256_crypt.hash(passwd)

    return phash


def verify_password(ngp: NgpBase) -> bool:
    """
    Verify user password
    """
    verify = False
    user = ngp.opts.user
    if user not in ngp.passwd_data:
        print('User is not in the password file - cannot check')
        return False

    phash = ngp.passwd_data[user]
    phash = phash.rstrip()
    verify = _hash_verify(ngp, phash)
    return verify
