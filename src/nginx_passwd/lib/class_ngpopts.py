# SPDX-License-Identifier: MIT
# Copyright (c) 2022,2023 Gene C
"""
NgpOpts  - command line options for nginx-passwd
"""
# pylint: disable=R0903

import os
import argparse
from .hash import hash_algo_default
from .hash import hash_algos_active
from .hash import hash_algos_deprecated

class NgpOpts:
    """
    Command line options
    """
    def __init__(self):
        desc = "nginx-passwd : nginx basic auth password manager"
        self.algo = None
        self.passwd_file = None
        self.passwd = None
        self.user = None
        self.delete = False
        self.verify = False

        algo_def = hash_algo_default()
        algos = hash_algos_active()
        algos_depr  = hash_algos_deprecated()
        self.algo = algo_def

        opts = [
                [('-f', '--passwd_file'),
                 {'help'        : 'Password file'}
                ],
                [('-a', '--algo'),
                 {'default'     : algo_def,
                  'help'        : f'def={algo_def} active={algos} deprecated={algos_depr}'}
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


        if self.algo in algos_depr:
            print(f'Warning: deprectated algo : {self.algo}')
        elif self.algo not in algos:
            print(f'Warning: unknown algo : {self.algo} - using {algo_def}')
            self.algo = algo_def

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
