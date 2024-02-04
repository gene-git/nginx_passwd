.. SPDX-License-Identifier: MIT

############
nginx-passwd
############

Overview
========


Key features
============

Basic Auth Password Manager.
Manages basic auth password files. This replaces the functionality provided by htpasswd from Apache.

###############
Getting Started
###############

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

nginx_passwd application
========================

Usage
-----

To add or modify a user and write the resulting password file:
.. code:: bash

    nginx-passwd -f <password_file> <user>

If file is not specified, then the result is written to stdout.

The supported algortithms are::

    * Modern : argon2, pbkdf2_sha512, pbkdf2_sha256
    * Active : sha512, sha256, bcrypt
    * Deprecated: md5,  md5_apr1

and sha256 is the default.

These older and now deprecated algorithms are still supported but should be replaced by
one of the active ones::

    md5 and md5_apr1 

where *md5_apr1*, also known as *apr1*, is the old apache variant of md5.

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

    Default is sha256. Can be one of::

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

Dependencies
============

* Run Time :

  * python (3.9 or later)
  * passlib

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

We follow the *live at head commit* philosophy. This means we recommend using the
latest commit on git master branch. We also provide git tags.

This approach is also taken by Google [1]_ [2]_.

License
=======

Created by Gene C. It is licensed under the terms of the MIT license.

 - SPDX-License-Identifier: MIT
 - Copyright (c) 2023, Gene C

.. _Github: https://github.com/gene-git/nginx_passwd
.. _Archlinux AUR: https://aur.archlinux.org/packages/nginx_passwd

.. [1] https://github.com/google/googletest  
.. [2] https://abseil.io/about/philosophy#upgrade-support


