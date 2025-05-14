# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2022-present  Gene C <arch@sapience.com>
"""
 Support library tools for nginx-passwd
"""
from typing import (Dict, IO)


def open_file(path: str, mode: str) -> IO | None:
    """
    Open a file and return file object

    Returns:
        IO | None:
        File object - IO = TextIO or BinaryIO
    """
    # pylint: disable=unspecified-encoding,consider-using-with
    try:
        fobj = open(path, mode)
    except OSError as err:
        print(f'Error opening file {path} : {err}')
        fobj = None
    return fobj


def read_passwd_file(file: str) -> Dict[str, str]:
    """
    Read into dictionary key is username
    """
    passwd_data: Dict[str, str] = {}

    fobj = open_file(file, 'r')
    if fobj:
        data = fobj.readlines()
        fobj.close()
    else:
        print(f'Failed to open password file for reading : {file}')
        return passwd_data

    for row in data:
        item = row.split(':', 1)
        if len(item) != 2:
            print(f'Skipping Bad line in password file: {row}')
            continue
        passwd_data[item[0]] = item[1]

    return passwd_data


def write_passwd_file(passwd_data: Dict[str, str], file: str):
    """
    Write dictionary to file
    """
    fobj = open_file(file, 'w')
    if not fobj:
        print(f'Failed to open password file for writing : {file}')
        return

    if not passwd_data:
        print('no data to print')
        fobj.close()
        return

    for item in passwd_data.items():
        user = item[0]
        passw = item[1]
        row = f'{user}:{passw}'
        fobj.write(row)
    fobj.close()


def print_passwd_file(passwd_data: Dict[str, str]):
    """
    Write dictionary to file
    """
    if not passwd_data:
        print('no data to print')
        return

    for item in passwd_data.items():
        user = item[0]
        passw = item[1]
        row = f'{user}:{passw}'
        print(row)
    return
