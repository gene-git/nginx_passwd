"""
Hash Tests
Please set PYTHONPATH.
"""
import os
from pathlib import Path
from pyconcurrent import run_prog


def _get_passinfo() -> tuple[str, str, str]:
    """
    Temporary Directory password file.
    """
    pid = os.getpid()
    uid = os.getuid()

    tmpdir = f'/tmp/_test-{uid}'
    os.makedirs(tmpdir, exist_ok=True)

    passuser = 'alice'
    password = 'xxx'
    passfile = f'{tmpdir}/secret.{pid}'

    return (passuser, password, passfile)


def _clean_file(path: str):
    """
    Remove file
    """
    if not path or not os.path.isfile(path):
        return
    try:
        os.unlink(path)
    except OSError:
        pass


def _test_hash(algo: str) -> bool:
    """
    Make new password, save to file
    Read file and verify.
    """
    pypath = os.getenv('PYTHONPATH')
    appdir = f'{pypath}/nginx_passwd_mod/apps'
    appdir = str(Path(f'{appdir}').resolve())

    (passuser, password, passfile) = _get_passinfo()
    pargs = [f'{appdir}/nginx-passwd.py']
    pargs += ['-f', passfile, '-p', password, '-a', algo]
    pargs += [passuser]

    (rc, _stdout, _stderr) = run_prog(pargs)
    if rc != 0:
        return False

    pargs += ['-v']
    (rc, _stdout, _stderr) = run_prog(pargs)
    _clean_file(passfile)

    if rc != 0:
        return False
    return True


class TestHash:
    """
    Hash test class
    """
    def test_bcrypt(self):
        """
        Test bcrypt
        """
        algo = 'bcrypt'
        assert _test_hash(algo)

    def test_sha512(self):
        """
        Test sha512
        """
        algo = 'sha512'
        assert _test_hash(algo)

    def test_sha256(self):
        """
        Test sha256
        """
        algo = 'sha256'
        assert _test_hash(algo)

    def test_pbkdf2_sha256(self):
        """
        Test pbkdf2_sha256
        """
        algo = 'pbkdf2_sha256'
        assert _test_hash(algo)

    def test_pbkdf2_sha512(self):
        """
        Test pbkdf2_sha512
        """
        algo = 'pbkdf2_sha512'
        assert _test_hash(algo)

    def test_argon2(self):
        """
        Test argon2
        """
        algo = 'argon2'
        assert _test_hash(algo)

    def test_md5(self):
        """
        Deprecated: Test md5
        """
        algo = 'md5'
        assert _test_hash(algo)

    def test_apr1(self):
        """
        Deprecated: Test apr1
        """
        algo = 'apr1'
        assert _test_hash(algo)
