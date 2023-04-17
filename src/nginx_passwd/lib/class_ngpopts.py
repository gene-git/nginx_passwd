# SPDX-License-Identifier: MIT
# Copyright (c) 2022,2023 Gene C
"""
NgpOpts  - command line options for nginx-passwd
"""
# pylint: disable=R0903

import os
import argparse

def _algo_map(algo):
    """
    Returns the openssl passwd option to use for this algo
    """
    algo_openssl = '-1'

    if not algo:
        return algo_openssl

    match(algo):
        case 'md5':
            algo_openssl = '-1'
        case 'apr1':
            algo_openssl = '-apr1'
        case 'sha256':
            algo_openssl = '-5'
        case 'sha512':
            algo_openssl = '-6'
        case _:
            algo_openssl = '-1'

    return algo_openssl

class NgpOpts:
    """
    Command line options
    """
    def __init__(self):
        desc = "nginx-passwd : nginx basic auth password manager"
        self.algo = 'md5'
        self.algo_openssl = '-1'
        self.passwd_file = None
        self.passwd = None
        self.user = None
        self.delete = False
        self.verify = False

        opts = [
                [('-f', '--passwd_file'),
                 {'help'        : 'Password file'}
                ],
                [('-a', '--algo'),
                 {'default'     : self.algo,
                  'help'        : 'Passord file'}
                ],
                [('-p', '--passwd'),
                 {'help'        : 'Password'}
                ],
                [('-D', '--delete'),
                 {'action'      : 'store_true',
                  'help'        : 'Delete this user'}
                ],
                [('-v', '--verify'),
                 {'action'      : 'store_true',
                  'help'        : 'Only Verify password - requires password file'}
                ],
                [('user', None),
                 {'nargs'       : '?',
                  'help'        : 'Username'}
                ],
               ]

        par = argparse.ArgumentParser(description=desc)
        for opt in opts:
            (opt_s, opt_l), kwargs = opt
            if opt_l :
                par.add_argument(opt_s, opt_l, **kwargs)
            else:
                par.add_argument(opt_s, **kwargs)

        parsed = par.parse_args()
        if parsed:
            # map to class attribute
            for (opt, val) in vars(parsed).items() :
                setattr(self, opt, val)

        self.algo_openssl = _algo_map(self.algo)

    def check(self):
        """
        sanity check
        """
        is_okay = True
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
