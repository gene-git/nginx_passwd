"""
Hash Tests

Please set PYTHONPATH.
"""
from typing import (Tuple)
import os

from .run_prog import run_prog


def _get_passinfo() -> Tuple[str, str, str]:
    """
    Temporary Directory password file.
    """
    pid = os.getpid()
    user = os.getlogin()

    tmpdir = f'/tmp/_test-{user}-{pid}'
    os.makedirs(tmpdir, exist_ok=True)

    passuser = 'alice'
    password = 'xxx'
    passfile = f'{tmpdir}/secret'

    return (passuser, password, passfile)


def _test_hash(algo: str) -> bool:
    """
    Make new password, save to file
    Read file and verify.

    """
    env = os.environ.copy()
    python_path = env.get('PYTHONPATH')
    if python_path:
        env['PATH'] = python_path + ':' + env['PATH']

    (passuser, password, passfile) = _get_passinfo()
    pargs = ['nginx-passwd.py']
    pargs += ['-f', passfile, '-p', password, '-a', algo]
    pargs += [passuser]

    (rc, _stdout, _stderr) = run_prog(pargs, env=env)
    if rc != 0:
        return False

    pargs += ['-v']
    (rc, _stdout, _stderr) = run_prog(pargs, env=env)
    if rc != 0:
        return False
    return True


class TestHash:
    """
    Hash test class
    """
    def test_active(self):
        """
        Test all active hash function
        """
        algos = ['argon2', 'pbkdf2_sha512', 'pbkdf2_sha256',
                 'sha512', 'sha256', 'bcrypt']

        for algo in algos:
            assert _test_hash(algo)

    def test_deprecated(self):
        """
        Test all deprecated hash function
        """
        algos = ['apr_md5', 'apr1', 'md5']

        for algo in algos:
            assert _test_hash(algo)
