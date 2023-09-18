# SPDX-License-Identifier: MIT
# Copyright (c) 2022,2023 Gene C
"""
 Generate password entry
"""
import getpass
# active
from passlib.hash import sha512_crypt
from passlib.hash import sha256_crypt
from passlib.hash import bcrypt
# deprecated
from passlib.hash import md5_crypt
from passlib.hash import apr_md5_crypt


# -------------
# Public
#
def get_passwd(ngp):
    """ get clear password """
    if ngp.opts.passwd :
        passwd =  ngp.opts.passwd
    else:
        passwd = getpass.getpass()
    return passwd

def hash_from_algo(algo):
    """ return the hash func to use """
    match algo:
        case 'bcrypt' :
            hash_func = bcrypt
        case 'sha512' :
            hash_func = sha512_crypt
        case 'sha256' :
            hash_func = sha256_crypt
        case 'sha512' :
            hash_func = sha256_crypt
        case 'md5' :
            hash_func = md5_crypt
        case 'apr_md5'|'apr1' :                 # apr1 for backward compat only
            hash_func = apr_md5_crypt
        case _:
            hash_func = sha256_crypt

    return hash_func

def hash_from_phash(phash):
    """ given a passwd hash, return the hash func to use """

    algos = hash_algos_active()
    algos += hash_algos_deprecated()
    for algo in algos:
        func = hash_from_algo(algo)
        if func.identify(phash):
            return func
    return None

def hash_verify(ngp, phash):
    """
    verify the hash
    """
    if not phash:
        return False
    passwd = get_passwd(ngp)
    hashf = hash_from_phash(phash)
    verify = False
    if hashf:
        verify = hashf.verify(passwd, phash)
    return verify

# -------------
# Public
#
def hash_algos_active():
    """ list of currently active hash functions """
    algos = ['bcrypt', 'sha256', 'sha512']
    return algos

def hash_algos_deprecated():
    """ list of deprecated but supported hash functions """
    depr = ['apr_md5', 'apr1', 'md5']
    return depr

def hash_algo_default():
    """ default algo to use of not specified """
    return 'sha256'

def generate_password(ngp, algo=None):
    """
    generate password hash item
    """
    if not algo:
        algo = hash_algo_default()

    passwd = get_passwd(ngp)
    hashf = hash_from_algo(algo)
    phash = hashf.hash(passwd)
    return phash

def verify_password(ngp):
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
    verify = hash_verify(ngp, phash)
    return verify
