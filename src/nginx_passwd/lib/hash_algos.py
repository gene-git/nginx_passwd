# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2022-present Gene C <arch@sapience.com>
"""
Hash algos and their ident strings
"""


def hash_algos_active() -> list[str]:
    """
    list of (currently) active hash functions
    Modern: 'argon2', 'pbkdf2_sha512', 'pbkdf2_sha256'
    Active: 'sha512', 'sha256', 'bcrypt'
    """
    modern = ['argon2', 'pbkdf2_sha512', 'pbkdf2_sha256']
    active = ['sha512', 'sha256', 'bcrypt']
    algos = modern + active
    return algos


def hash_algos_deprecated() -> list[str]:
    """
    list of deprecated but supported hash functions
    apr1 is identical to md5 - since "password + salt + ident" is
    what gets hashed, this is not interchanable with plain md5
    due to presence of ident string. Pretty silly idea really.
    "apr_md5" is alternative name for "apr1"
    """
    algos = ['apr1', 'apr_md5', 'md5']
    return algos


def hash_algo_default() -> str:
    """
    default algo to use when not specified
    At some point we should change this to 'argon2'
    """
    return 'sha256'


def hash_to_ident(phash: str) -> str:
    """
    Determine the algo used to make this password hash
    from the ident string.
    phash ~ "$ident$..."

    Args:
        phash (str):
            The hashed password
    Return:
        str:
            The password hash algorithm.
    """
    algo = ''
    if not phash:
        return algo

    if phash.startswith('$argon2id$'):
        algo = 'argon2'

    elif phash.startswith('$pbkdf2-sha512$'):
        algo = 'pbkdf2-sha512'

    elif phash.startswith('$pbkdf2-sha256$'):
        algo = 'pbkdf2-sha256'

    elif phash.startswith('$2b$'):
        algo = 'bcrypt'

    elif phash.startswith('$6$'):
        algo = 'sha512'

    elif phash.startswith('$5$'):
        algo = 'sha256'

    elif phash.startswith('$apr1$'):
        algo = 'apr1'

    elif phash.startswith('$1$'):
        algo = 'md5'

    return algo
