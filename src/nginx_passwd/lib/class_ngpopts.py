# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2022-present  Gene C <arch@sapience.com>
"""
NgpOpts  - command line options for nginx-passwd
"""
# pylint: disable=too-few-public-methods
import os

from ._ngpopts_base import NgpOptsBase
from .opts import parse_options
from .utils import open_file


class NgpOpts(NgpOptsBase):
    """
    Command line options
    """
    def __init__(self):
        super().__init__()

        parse_options(self)

    def check(self) -> bool:
        """
        sanity check

        Returns:
            bool:
            True if all ok otherwise False
        """
        is_okay = True
        if not self.user:
            print(' A user name is required - please provide one')
            is_okay = False

        if self.passwd_file and not os.path.exists(self.passwd_file):
            print(f' New password file: {self.passwd_file}')
            fob = open_file(self.passwd_file, 'w')
            if fob:
                fob.close()
            else:
                print(f' Cannot create password file: {self.passwd_file}')
                is_okay = False

        if self.delete and not self.passwd_file:
            print(' Delete a user requires password file')
            is_okay = False

        if self.verify and not self.passwd_file:
            print(' Verify user password requires password file')
            is_okay = False

        return is_okay
