# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2022-present Gene C <arch@sapience.com>
"""
sha256 rounds = 535000
sha512 rounds = 656000

"""
import os
from dataclasses import dataclass
from base64 import b64encode, b64decode

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf import pbkdf2
from cryptography.hazmat import backends


@dataclass
class Pbkdf2Data:
    """ Data Package for pbkdf2 """
    ident: str = ''
    salt: bytes = b''
    iterations: int = 0
    length: int = 0


def _pbkdf2_password_hash(passwd: str, data: Pbkdf2Data) -> str:
    """
    Generates SHA256 password hash using PBKDF2HMAC.

    Args:
        passwd (str):
            The password string.

        data (Pbkdf2Data):
            Provides: salt, algo string, iterations, length and ident

    Returns:
            (str):
                The password hash
    """
    passwd_bytes: bytes = passwd.encode('utf-8')

    #
    # - 12 bytes for salt will lead to 16 characters (sha256)
    # - 16 bytes of salt will lead to 22 characters (sha512)
    #
    salt = data.salt
    length = data.length
    iterations = data.iterations
    ident = data.ident

    algorithm: hashes.SHA512 | hashes.SHA256
    match data.ident:
        case 'pbkdf2-sha256':
            algorithm = hashes.SHA256()
        case 'pbkdf2-sha512':
            algorithm = hashes.SHA512()
        case _:
            algorithm = hashes.SHA256()

    kdf = pbkdf2.PBKDF2HMAC(
            algorithm=algorithm,
            length=length,
            salt=salt,
            iterations=iterations,
            backend=backends.default_backend()
            )
    key = kdf.derive(passwd_bytes)

    #
    # Hash into base64 strings in password file format
    #
    salt_b64 = b64encode(salt).decode('utf-8').rstrip('=')
    key_b64 = b64encode(key).decode('utf-8').rstrip('=')

    pass_hash = f'${ident}${iterations}${salt_b64}${key_b64}'

    return pass_hash


def _parse_password_hash(phash: str) -> Pbkdf2Data:
    """
    Parse the password hash into it's components
    """
    pbkdata: Pbkdf2Data = Pbkdf2Data()

    if not phash:
        return pbkdata

    parts = phash[1:].split('$')
    if len(parts) < 4:
        return pbkdata

    ident = parts[0]
    iterations: int = int(parts[1])
    salt_b64 = parts[2]
    salt = b64decode((salt_b64 + '==').encode('utf-8'))

    pbkdata.ident = ident
    length = 32
    match ident:
        case 'pbkdf2-sha512':
            length = 64
        case 'pbkdf2-sha256':
            length = 32
        case _:
            length = 32

    pbkdata.iterations = iterations
    pbkdata.salt = salt
    pbkdata.length = length

    return pbkdata


def _pbkdf2_verify_password(phash: str, passwd: str) -> bool:
    """
    Verify pbkdf2_sha356 password
    """
    if not phash:
        return False

    pbkdata = _parse_password_hash(phash)
    if not pbkdata.ident:
        return False

    phash_check = _pbkdf2_password_hash(passwd, pbkdata)

    verify: bool = False
    if phash == phash_check:
        verify = True

    return verify

#
# Public Entry Points
#


def pbkdf2_sha256_verify_password(phash: str, passwd: str) -> bool:
    """
    Verify pbkdf2_sha256
    """
    return _pbkdf2_verify_password(phash, passwd)


def pbkdf2_sha512_verify_password(phash: str, passwd: str) -> bool:
    """
    Verify pbkdf2_sha512
    """
    return _pbkdf2_verify_password(phash, passwd)


def pbkdf2_sha256_password_hash(passwd: str) -> str:
    """
    Generate password hash for pbkdf2-sha256
    """
    salt = os.urandom(12)

    # num_rounds = 535000
    num_rounds = 29000

    pbkdata: Pbkdf2Data = Pbkdf2Data(
            ident='pbkdf2-sha256',
            iterations=num_rounds,
            length=32,
            salt=salt,
            )

    pass_hash = _pbkdf2_password_hash(passwd, pbkdata)
    return pass_hash


def pbkdf2_sha512_password_hash(passwd: str) -> str:
    """
    Generate password hash for pbkdf2-sha256
    """
    salt = os.urandom(16)

    num_rounds = 25000

    pbkdata: Pbkdf2Data = Pbkdf2Data(
            ident='pbkdf2-sha512',
            iterations=num_rounds,
            length=64,
            salt=salt,
            )

    pass_hash = _pbkdf2_password_hash(passwd, pbkdata)
    return pass_hash
