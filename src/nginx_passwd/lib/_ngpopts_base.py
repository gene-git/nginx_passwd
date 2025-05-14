# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2022-present  Gene C <arch@sapience.com>
"""
NgpOpts  - command line options for nginx-passwd
"""
# pylint: disable=too-few-public-methods


class NgpOptsBase:
    """
    Command line options base class (the data)
    """
    def __init__(self):
        self.algo: str = ''
        self.passwd_file: str = ''
        self.passwd: str = ''
        self.user: str = ''
        self.delete: bool = False
        self.verify: bool = False
