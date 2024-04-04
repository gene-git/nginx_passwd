# SPDX-License-Identifier: MIT
# Copyright (c) 2022,2023 Gene C
"""
NgpOpts  - command line options for nginx-passwd
"""
# pylint: disable=R0903

import os
from .opts import parse_options

class NgpOpts:
    """
    Command line options
    """
    def __init__(self):
        self.algo = None
        self.passwd_file = None
        self.passwd = None
        self.user = None
        self.delete = False
        self.verify = False

        parse_options(self)

    def check(self):
        """
        sanity check
        """
        is_okay = True
        if not self.user :
            print(f' A user name is required - please provide one')
            is_okay = False

        if self.passwd_file and not os.path.exists(self.passwd_file):
            print(f' Password file not found : {self.passwd_file}')
            is_okay = False

        if self.delete and not self.passwd_file:
            print(' Delete a user requires password file')
            is_okay = False

        if self.verify and not self.passwd_file:
            print(' Verify user password requires password file')
            is_okay = False

        return is_okay
