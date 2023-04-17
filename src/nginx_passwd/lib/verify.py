# SPDX-License-Identifier: MIT
# Copyright (c) 2022,2023 Gene C
"""
 Check password in password file for one user
"""
from .generate_passwd import generate_password

def verify_password(ngp):
    """
    Verify password for user
    """
    verify = False
    user = ngp.opts.user
    if user not in ngp.passwd_data:
        print('User is not in the password file - cannot check')
        return False

    item_file = ngp.passwd_data[user]
    item_file = item_file.rstrip()
    (algo, salt, _pass_hash_file) = extract_pw_info(item_file)
    algo_openssl = f'-{algo}'

    item = generate_password(ngp, algo=algo_openssl, salt=salt)
    item = item.rstrip()

    if item == item_file:
        verify = True
    return verify

def extract_pw_info(this_item):
    """
    each item takes form:
        user:$algo$alt$password_hash
    """
    algo = None
    salt = None
    pass_hash = None

    if not this_item:
        return (algo, salt, pass_hash)

    this_split = this_item.split('$', 3)
    if len(this_split) < 1:
        return (algo, salt, pass_hash)

    algo = this_split[1]
    if len(this_split) > 2:
        salt = this_split[2]
        if len(this_split) > 3:
            pass_hash = this_split[3]
            pass_hash.rstrip()

    return (algo, salt, pass_hash)
