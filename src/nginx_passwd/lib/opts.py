# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2022-present  Gene C <arch@sapience.com>
"""
Available options
"""
# pylint: disable=

import sys
import argparse
from .hash import hash_algo_default
from .hash import hash_algos_active
from .hash import hash_algos_deprecated

def get_available_options(algo_def:str, algos:[str], algos_depr:[str]):
    """
    List of command line options for argparse
    """
    prog = sys.argv[0]
    argv = sys.argv[1:]
    desc = "nginx-passwd : nginx basic auth password manager"


    opts = []
    act = 'action'
    act_on = 'store_true'

    ohelp = 'Password file'
    opt = [('-f', '--passwd_file'), {'help' : ohelp}]
    opts.append(opt)

    ohelp = f'default={algo_def} active={algos} deprecated={algos_depr}'
    opt = [('-a', '--algo'), {'help' : ohelp, 'default' : algo_def}]
    opts.append(opt)

    ohelp = 'Passowrd to use '
    opt = [('-p', '--passwd'), {'help' : ohelp}]
    opts.append(opt)

    ohelp = 'Delete this user'
    opt = [('-D', '--delete'), {'help' : ohelp, act : act_on}]
    opts.append(opt)

    ohelp = 'Only Verify password - requires password file'
    opt = [('-v', '--verify'), {'help' : ohelp, act : act_on}]
    opts.append(opt)

    ohelp = 'Username'
    opt = [('user', None), {'help' : ohelp, 'nargs' : '?'}]
    opts.append(opt)

    return (prog, desc, argv, opts)

def parse_options(ngp:'NgpOpts') :
    """
    Parse command line options 
    """
    algo_def = hash_algo_default()
    algos = hash_algos_active()
    algos_depr  = hash_algos_deprecated()

    #
    # Get options
    #
    (prog, desc, argv, opts) = get_available_options(algo_def, algos, algos_depr)

    #
    # Parse and save
    #
    par = argparse.ArgumentParser(description=desc, prog=prog)

    for opt in opts:
        (opt_s, opt_l), kwargs = opt
        if opt_l :
            par.add_argument(opt_s, opt_l, **kwargs)
        else:
            par.add_argument(opt_s, **kwargs)

    parsed = par.parse_args(argv)
    if parsed:
        # map to class attribute
        for (opt, val) in vars(parsed).items() :
            setattr(ngp, opt, val)

    if ngp.algo in algos_depr:
        print(f'Warning: deprectated algo : {ngp.algo}')
    elif ngp.algo not in algos:
        print(f'Warning: unknown algo : {ngp.algo} - using {ngp}')
        ngp.algo = algo_def
