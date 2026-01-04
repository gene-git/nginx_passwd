.. SPDX-License-Identifier: GPL-2.0-or-later

############
nginx-passwd
############

Overview
========

Basic Auth Password Manager.
Manages basic auth password files. This replaces the functionality provided by htpasswd from Apache.
It also provides modern hash functions, such as argon2 and pbkdf2_sha512, which are far superior.


* All git tags are signed with arch@sapience.com key which is available via WKD
  or download from https://www.sapience.com/tech. Add the key to your package builder gpg keyring.
  The key is included in the Arch package and the source= line with *?signed* at the end can be used
  to verify the git tag.  You can also manually verify the signature

New Or Interesting
==================

**Version 3.3.0**

* Source code reorg
* Switch python packager from hatch to uv
* Confirm all working with python 3.14.2

**Version 3.1.0**

* Remove os.getlogin() in tests (ENOTTY reported by @ccharabaruk on AUR package).
* Small tidy ups

**Version 3.0.0**

* Reduce our reliance on passlib (it is unmaintained).

  * passlib bcrypt is broken 
  * there is a fork which works

* Algo changes - limit use of passlib only to legacy hashes
  
  * bcrypt : now uses python-bcrypt directly
  * argon2 : now uses python-argon2-cffi (which calls C library)
  * pbkdf2_sha512 : now uses python-cryptography
  * pbkdf2_sha256 : now uses python-cryptography
  * md5_crypt : legacy algo using passlib
  * apr_md5_crypt : legacy algo using passlib

**Older**

* PEP-8, PEP-257, PEP-484 and PEP 561
* Refactor code
* Add pytests
* add python-bcrypt dependency to Arch PKBUILD
* For simplicity, make argon2 required instead of optional


###############
Getting Started
###############


nginx_passwd application
========================

Usage
-----

To add or modify a user and write the resulting password file:

.. code-block:: bash

    nginx-passwd -f <password_file> <user>

If file is not specified, then the result is written to stdout.

The supported algortithms are::

    * Modern : argon2, pbkdf2_sha512, pbkdf2_sha256
    * Active : sha512, sha256, bcrypt
    * Deprecated: md5,  apr_md5/apr1

with *sha256* being the default. 

Note: At some point in futute we will change the default algo to the more modern *argon2*.

Older and now deprecated algorithms (*md5*, *apr_md5*) are still supported but should be replaced by
one of the active ones.

Note: *apr_md5*, also known as *apr1*, is the ancient Apache variant of md5.

Note: If the password is not provided with *-p* option and is nowhere is found to read it from, then it will
be an empty string. 

Options
-------

The options are given below and *nginx-passwd -h* provides a help summary.

Positional Argument:

* username

   required argument.

* (*-h, --help*)

   show help message and exit

* (*-f, --passwd_file*)  <password_file>   

  Write to this Password file

* (*-a, --algo*) <algorithm>   

  Default is now argon2 (older versions used sha256). Can be one of::

  * Modern : argon2, pbkdf2_sha512, pbkdf2_sha256
  * Active : sha512, sha256, bcrypt
  * Deprecated: md5,  md5_apr1

* (*-p, --passwd*) <password>  

  Password as an option. Without this it will be read from stdin.

* (*-D, --delete*)

  Delete this user from the password file.

* (*-v, --verify*)

  Checks that the provided password matches that in the password file

########
Appendix
########

Installation
============

Available on
* `Github`_
* `Archlinux AUR`_

On Arch you can build using the PKGBUILD provided in packaging directory or from the AUR package.
To build manually, clone the repo and do:

.. code-block:: bash
   :caption: Manual Install

        rm -f dist/*
        /usr/bin/python -m build --wheel --no-isolation
        root_dest="/"
        ./scripts/do-install $root_dest

When running as non-root then set root\_dest a user writable directory

Dependencies
============

* Run Time :

  * python          (3.13 or later)
  * passlib
  * bcrypt          (aka python-bcrypt)
  * argon2-cffi     (aka python-argon2-cffi)
  * cryptography    (aka python-cryptography)


*NB* versions 1.1 and earlier used openssl - all newer version now use python passlib library.

* Building Package:

  * git
  * hatch           (aka python-hatch)
  * wheel           (aka python-wheel)
  * build           (aka python-build)
  * installer       (aka python-installer)
  * rsync

* Optional for building docs:

  * sphinx
  * texlive-latexextra  (archlinux packaguing of texlive tools)

Philosophy
==========

We follow the *live at head commit* philosophy as recommended by
Google's Abseil team [1]_.  This means we recommend using the
latest commit on git master branch. 


License
=======

Created by Gene C. It is licensed under the terms of the GPL-2.0-or-later license.

 - SPDX-License-Identifier: GPL-2.0-or-later
 - SPDX-FileCopyrightText: © 2023-present  Gene C <arch@sapience.com>

.. _Github: https://github.com/gene-git/nginx_passwd
.. _Archlinux AUR: https://aur.archlinux.org/packages/nginx_passwd

.. [1] https://abseil.io/about/philosophy#upgrade-support


