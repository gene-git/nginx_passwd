# SPDX-License-Identifier: MIT
# Copyright (c) 2022,2023 Gene C
"""
 Update password dictionary
"""

def passwd_data_delete_user(passwd_data, user):
    """
    Remove user from password data
    """
    if not passwd_data:
        return passwd_data

    if user in passwd_data:
        del passwd_data[user]

    return passwd_data

def passwd_data_update_user(passwd_data, user, passwd_item):
    """
    Add or modify user's password
    """
    if not passwd_data:
        passwd_data = {user : passwd_item}

    else:
        passwd_data[user] = passwd_item

    return passwd_data
