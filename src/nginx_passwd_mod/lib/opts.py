# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2022-present Gene C <arch@sapience.com>
"""
Available options
"""
# pylint: disable=too-many-locals
from typing import (Any)
import sys
import argparse

from ._ngpopts_base import NgpOptsBase
from .hash_algos import hash_algo_default
from .hash_algos import hash_algos_active
from .hash_algos import hash_algos_deprecated
from .hash_algos import hash_algos_modern

type Opt = tuple[str | tuple[str, str], dict[str, Any]]


def _avail_options(algo_def: str, algos_depr: str, algos_act: str, algos_mod: str
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

    ohelp = f'Default is {algo_def}'
    ohelp += f'\n* modern     : {algos_mod}'
    ohelp += f'\n* active     : {algos_act}'
    ohelp += f'\n* deprecated : {algos_depr}'
    ohelp += '\nAlgo names may use "_" or "-"'
    opts.append((('-a', '--algo'), {'help': ohelp, 'default': algo_def}))

    ohelp = 'Password to use'
    opts.append((('-p', '--passwd'), {'help': ohelp}))

    ohelp = 'Delete this user'
    opts.append((('-D', '--delete'), {'help': ohelp, 'action': 'store_true'}))

    ohelp = 'Only Verify password - requires password file'
    opts.append((('-v', '--verify'), {'help': ohelp, 'action': 'store_true'}))

    ohelp = 'Username'
    opts.append(('user', {'help': ohelp, 'nargs': '?'}))

    return (prog, desc, argv, opts)


def parse_options(ngp: NgpOptsBase):
    """
    Parse command line options
    """
    #
    # All algos display with hyphen not underscore - we accept either
    #
    algo_def = hash_algo_default()

    algos_mod = hash_algos_modern()
    algos_mod = [algo.replace('_', '-') for algo in algos_mod]
    algos_mod_str = ', '.join(algos_mod)

    algos_act = hash_algos_active()
    algos_act = [algo.replace('_', '-') for algo in algos_act]
    algos_act_str = ', '.join(algos_act)

    algos_depr = hash_algos_deprecated()
    algos_depr = [algo.replace('_', '-') for algo in algos_depr]
    algos_depr_str = ', '.join(algos_depr)

    #
    # Get options
    #
    (prog, desc, argv, opts) = _avail_options(algo_def, algos_depr_str, algos_act_str, algos_mod_str)

    #
    # Parse and save
    #
    par = argparse.ArgumentParser(
            description=desc,
            formatter_class=argparse.RawTextHelpFormatter,
            prog=prog)

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

    #
    # Algo check
    #
    if ngp.algo in algos_depr:
        print(f'Warning: deprectated algo: {ngp.algo}')

    elif ngp.algo not in algos_mod + algos_act:
        print(f'Warning: unknown algo: {ngp.algo} - using {ngp}')
        ngp.algo = algo_def
