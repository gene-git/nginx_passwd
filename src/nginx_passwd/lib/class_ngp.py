# SPDX-License-Identifier: MIT
# Copyright (c) 2022,2023 Gene C
"""
nginx-passwd class
"""
from .class_ngpopts import NgpOpts
from .utils import read_passwd_file
from .utils import write_passwd_file
from .utils import print_passwd_file
from .hash import generate_password
from .update import passwd_data_delete_user
from .update import passwd_data_update_user
from .hash import verify_password

class Ngp:
    """
    nginx-passwd manager class
    """
    # pylint: disable=R0903
    def __init__(self):

        self.opts = NgpOpts()
        self.passwd_data = None
        self.passwd_item = None

        if not self.opts.check():
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
            self.passwd_data = passwd_data_update_user(self.passwd_data, user, self.passwd_item)

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
