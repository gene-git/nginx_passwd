# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2022-present  Gene C <arch@sapience.com>
"""
Available options
"""
# pylint: disable=
from typing import (Any)
import sys
import argparse

from ._ngpopts_base import NgpOptsBase
from .hash_algos import hash_algo_default
from .hash_algos import hash_algos_active
from .hash_algos import hash_algos_deprecated

type Opt = tuple[str | tuple[str, str], dict[str, Any]]


def _avail_options(algo_def: str, algos: list[str],
                   algos_depr: list[str]
                   ) -> tuple[str, str, list[str], list[Opt]]:
    """
    List of command line options for argparse
    """
    prog = sys.argv[0]
    argv = sys.argv[1:]

    desc = "nginx-passwd: nginx basic auth password manager"
    opts: list[Opt] = []

    ohelp = 'Password file'
    opt = (('-f', '--passwd_file'), {'help': ohelp})
    opts.append(opt)

    ohelp = f'default={algo_def} active={algos} deprecated={algos_depr}'
    opt = (('-a', '--algo'), {'help': ohelp, 'default': algo_def})
    opts.append(opt)

    ohelp = 'Passowrd to use '
    opt = (('-p', '--passwd'), {'help': ohelp})
    opts.append(opt)

    ohelp = 'Delete this user'
    opts.append((('-D', '--delete'),
                 {'help': ohelp, 'action': 'store_true'}))

    ohelp = 'Only Verify password - requires password file'
    opts.append((('-v', '--verify'),
                 {'help': ohelp, 'action': 'store_true'}))

    ohelp = 'Username'
    opts.append(('user', {'help': ohelp, 'nargs': '?'}))

    return (prog, desc, argv, opts)


def parse_options(ngp: NgpOptsBase):
    """
    Parse command line options
    """
    algo_def = hash_algo_default()
    algos = hash_algos_active()
    algos_depr = hash_algos_deprecated()

    #
    # Get options
    #
    (prog, desc, argv, opts) = _avail_options(algo_def, algos,
                                              algos_depr)

    #
    # Parse and save
    #
    par = argparse.ArgumentParser(description=desc, prog=prog)

    for opt in opts:
        opt_list, kwargs = opt
        if isinstance(opt_list, str):
            par.add_argument(opt_list, **kwargs)
        else:
            par.add_argument(*opt_list, **kwargs)

    parsed = par.parse_args(argv)
    if parsed:
        # map dictionary to class attribute
        for (key, val) in vars(parsed).items():
            setattr(ngp, key, val)

    if ngp.algo in algos_depr:
        print(f'Warning: deprectated algo: {ngp.algo}')

    elif ngp.algo not in algos:
        print(f'Warning: unknown algo: {ngp.algo} - using {ngp}')
        ngp.algo = algo_def
