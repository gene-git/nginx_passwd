# nginx-passwd

Basic Auth Password Manager.

Tool to help manage basic auth password files. This replaces the functionality provided by htpasswd from Apache.


## Installation

Available on
 - [Github source ](https://github.com/gene-git/nginx_passwd)
 - [Archlinux AUR](https://aur.archlinux.org/packages/nginx_passwd)

If on Arch can build using the PKGBUILD provided which is also available in the AUR.

To build it manually, clone the repo and do:

        rm -f dist/*
        /usr/bin/python -m build --wheel --no-isolation
        root_dest="/"
        ./scripts/do-install $root_dest

  If running as non-root then set root\_dest a user writable directory


### Dependencies

- Run Time :
  - python (3.9 or later)
  - passlib

NB versions 1.1 and earlier used openssl - all newer version nuse python passlib library.

```

## Overview

To add or modify a user and write the resulting password file:

    nginx-passwd -f <password_file> <user>

If file is not specified, then the result is written to stdout.

The active algortithms are:

    bcrypt, sha256 and sha512

and sha256 being is the default.
Older algorithms which are still supported but are deprecated and should be replaced by
one of the active ones:

    md5 and md5_apr1 

md5_apr1, also known as apr1, is the apache variant of md5.

See options below or *nginx-passwd -h* for help.

### Options

    username        - required positional argument.

  - *-h, --help*   
     show help message and exit

  - *-f, --passwd_file*  <password_file>   
    Use this Password file

  - *-a, --algo* <algorithm>   
    Default is sha256   
    Can be:  md5, sha256, sha512 (md5 and md5_apr1) are considered deprecated

  - *-p, --passwd* <password>  
    Password as an option. Without this it will be read from stdin.

  - *-D, --delete*   
    Delete this user from the password file.

  - *-v, --verify*    
    Checks that the provided password matches that in the password file

## License

Created by Gene C. It is licensed under the terms of the MIT license.

 - SPDX-License-Identifier: MIT
 - Copyright (c) 2023, Gene C
