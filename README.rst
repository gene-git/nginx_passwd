
============
nginx-passwd
============

Overview
========

Basic Auth Password Manager.

Manages basic auth password files. This replaces the functionality provided by htpasswd from Apache.
It also provides legacy and modern hash functions, including the argon2 and pbkdf2_sha512.


* All git tags are signed with arch@sapience.com key which is available via WKD
  or download from https://www.sapience.com/tech. Add the key to your package builder gpg keyring.
  The key is included in the Arch package and the source= line with *?signed* at the end can be used
  to verify the git tag.  You can also manually verify the signature

Recent Changes
==============

**Version 4.0.1**

* Remove sphinx tmp files from html docs
* Make pytest optional in meson.build

**Version 4.0.0**

* Default hash algo is argon2
* Use meson / meson python for build and package management
* Periodic code review
* tests use (and check depends) on pyconcurrent package.

Note on Hash Functions
======================

Wa minimize reliance on passlib since it is unmaintained and its bcrypt functions are 
broken. Hash functions are separated into *modern*, *active* and *deprecated*. 
Modern are strongly preferred while active are okay. Deprecated algos should be avoided.

**Modern**

 =============  ===========
 Algo           Module Used
 =============  ===========
 argon2         python-argon2-cffi (via C library)
 pbkdf2_sha512  python-cryptography
 pbkdf2_sha256  python-cryptography
 bcrypt         python-bcrypt 
 =============  ===========

**Active**

 =============  ===========
 Algo           Module Used
 =============  ===========
 sha512         passlib
 sha256         passlib
 =============  ===========

**Deprecated / Legacy**

 =============  ===========
 Algo           Module Used
 =============  ===========
 md5_crypt      passlib
 apr_md5_crypt  using passlib
 =============  ===========


Getting Started
===============

The nginx-passwd application manages a password file with usernames and their hashed passwords.

Usage
-----

To add or modify a user and write the resulting password file::

    nginx-passwd -f <password_file> <user>

If file is not specified, then the result is written to stdout.

The supported hash algortithms as noted above are::

    * Modern : argon2, pbkdf2_sha512, pbkdf2_sha256
    * Active : sha512, sha256, bcrypt
    * Deprecated: md5,  apr_md5/apr1

with *argon2* the default with version *4.0.0* and newer. In older versions *sha256* was the default. 

Older and now deprecated algorithms (*md5*, *apr_md5*) are still supported but really should 
be avoided and replaced by one of the modern/active ones.

The *apr_md5* algo, also known as *apr1*, is the ancient Apache variant of md5.

If a password is not provided with *-p* option or from stdin, then it will be an empty string. 

Options
-------

The options are given below and *nginx-passwd -h* provides a help summary::

    positional arguments:
      user                      Username

    options:
      -h, --help                show this help message and exit
      -f, --passwd_file <file>  Password file
      -a, --algo ALGO           Defaults to argon2.
                                * Modern : argon2, pbkdf2-sha512, pbkdf2-sha256
                                * Active : sha512, sha256, bcrypt
                                * Deprecated: md5,  apr-md5/apr1
                                Algo names may use "_" or "-"
      -p, --passwd PASSWD       Password to use
      -D, --delete              Delete this user
      -v, --verify              Only Verify password - requires password file

