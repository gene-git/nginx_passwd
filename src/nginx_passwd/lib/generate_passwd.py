# SPDX-License-Identifier: MIT
# Copyright (c) 2022,2023 Gene C
"""
 Generate password entry
"""
import getpass
from .run_prog import run_prog

def generate_password(ngp, algo=None, salt=None):
    """
    Use openssl to generate the password item
    algo is openssl option which determines algo choice
    """

    prog = ['/usr/bin/openssl', 'passwd', '-noverify', '-stdin']
    if salt:
        prog += ['-salt', salt]
    if algo:
        prog += [algo]
    else:
        prog += [ngp.opts.algo_openssl]

    if ngp.opts.passwd :
        this_passwd =  ngp.opts.passwd
    else:
        this_passwd = getpass.getpass()

    # keep password away from command line
    [ret, output, err] = run_prog(prog, input_str=this_passwd)
    if ret != 0:
        print('Failed to geneate new password')
        print(err)
        return None
    pass_item = output
    return pass_item
