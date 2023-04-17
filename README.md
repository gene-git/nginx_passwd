# nginx-passwd

Basic Auth Password Manager
Manage basic auth password files. This replaces the functionality provided by htpasswd from Apache.


## Installation

Available on
 - [Github source ](https://github.com/gene-git/nginx_passwd)
 - [Archlinux AUR](https://aur.archlinux.org/packages/nginx_passwd)

If on Arch can build using the PKGBUILD provided which is also available in the AUR.

To build it manually, clone the repo and do:

        rm -f dist/*
        poetry build --format wheel
        root_dest="/"
        ./scripts/do-install $root_dest

  If running as non-root then set root\_dest a user writable directory


### Dependencies

- Run Time :
  - python (3.9 or later)
  - openssl (used to generate passwords)

```

## Overview

To add or modify a user and write the resulting password file:

    nginx-passwd -f <password_file> <user>

With specifying a file, the result is written to stdout.
The default algorithm uses md5. See options for more information.


### Options

    username        - required positional argument.

  - *-h, --help*   
     show help message and exit

  - *-f, --passwd_file*  <password_file>   
    Use this Password file

  - *-a, --algo* <algorithm>   
    Default is md5   
    Can be:  md5, sha256, sha512 or apr1

  - *-p, --passwd* <password>  
    Password as an option. Without this it will be read from stdin.

  - *-D, --delete*   
    Delete this user from the password file.

## License

Created by Gene C. It is licensed under the terms of the MIT license.

 - SPDX-License-Identifier: MIT
 - Copyright (c) 2023, Gene C
