# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2022-present  Gene C <arch@sapience.com>
"""
nginx-passwd class
"""
from ._ngp_base import NgpBase
from .utils import write_passwd_file
from .utils import print_passwd_file
from .utils import read_passwd_file
from .hash import generate_password
from .update import passwd_data_delete_user
from .update import passwd_data_update_user
from .hash import verify_password


class Ngp(NgpBase):
    """
    nginx-passwd manager class

    Child class with methods.
    Using base class with data allows using separate
    files to perform actions while avoiding circular
    import issues.
    """
    def __init__(self):
        super().__init__()

        if not self.opts.check():
            self.okay = False
            return

        if self.opts.passwd_file:
            self.passwd_data = read_passwd_file(self.opts.passwd_file)

    def update(self):
        """
        Update passwd_data
          - delete username if specified
          - add / modify otherwise
        """
        user = self.opts.user
        if self.opts.delete:
            self.passwd_data = passwd_data_delete_user(self.passwd_data, user)
        else:
            self.passwd_item = generate_password(self, algo=self.opts.algo)
            self.passwd_data = passwd_data_update_user(self.passwd_data,
                                                       user, self.passwd_item)

        if self.opts.passwd_file:
            write_passwd_file(self.passwd_data, self.opts.passwd_file)
        else:
            print_passwd_file(self.passwd_data)

    def verify(self):
        """
        Check the password for user
        """
        is_match = verify_password(self)
        if is_match:
            print('Password matches')
        else:
            print('Password NOT a match')

    def doit(self):
        """
        Update or verify
        """
        if self.opts.verify:
            self.verify()
        else:
            self.update()
