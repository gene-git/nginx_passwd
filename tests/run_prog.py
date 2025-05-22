"""
 run_prog.py

 Run program return status and stdout and stderr

 gc
   2022-04-17
"""
# pylint: disable=subprocess-run-check
from typing import (Any)
import subprocess


def run_prog(pargs: list[str], env: dict[str, str] | None
             ) -> tuple[int, str, str]:
    """
    run external program using subprocess
        pargs = [cmd, arg1, arg2, ... ]
    """
    retc = 0
    output = ''
    errors = ''

    run_args: dict[str, Any] = {
            'stdout': subprocess.PIPE,
            'stderr': subprocess.PIPE,
            'text': True,
            'check': False,
            }
    if env:
        run_args['env'] = env

    if pargs and pargs != []:
        try:
            ret = subprocess.run(pargs, **run_args)
            retc = ret.returncode
            output = ret.stdout
            errors = ret.stderr

        except subprocess.CalledProcessError:
            pass

        except FileNotFoundError:
            pass
        #    errors = str(ret.stderr, 'utf-8',errors='ignore')

    return (retc, output, errors)
