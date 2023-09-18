#!/usr/bin/python3
"""
  Basic Auth Password manager - replacement for Apache htpasswd
  NB arguments are different than htpasswd

  nginx-passwd -algo <algo>  -f password_file -p password username

    -algo  <alg>     - md5,apr1 supported algorithm - default is md5
    -p     <pass>    - password on command line, without this read it from stdin
    -f  <pass_file>  - password file to be edited. If not set, write to stdoutput
    -D               - delete this username

    Basic Auth Password files are in form:
    username:<password info>
"""
# pylint: disable=invalid-name
#import pdb
from lib import Ngp

def main():
    """
    nginx-passwd
       replacement for htpasswd
    """
    #pdb.set_trace()
    ngp = Ngp()
    ngp.doit()

# -----------------------------------------------------
if __name__ == '__main__':
    main()
# -------------------- All Done ------------------------
