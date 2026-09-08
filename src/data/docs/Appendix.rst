
========
Appendix
========

Installation
============

Available on
* `Github <https://github.com/gene-git/nginx_passwd>`_
* `Archlinux AUR <https://aur.archlinux.org/packages/nginx_passwd>`_

On Arch you can build using the PKGBUILD provided in packaging directory or from the AUR package.
To build manually, clone the repo and do::

        ./scripts/do-build
        ./scripts/do-install <destination-directory>

Dependencies
============

* Run Time :

  * python
  * passlib
  * bcrypt
  * argon2-cffi
  * cryptography

* Building Package:

  * git
  * meson
  * meson-python
  * rsync

=======

Created by Gene C. It is licensed under the terms of the GPL-2.0-or-later license.

 - SPDX-License-Identifier: GPL-2.0-or-later
 - SPDX-FileCopyrightText: © 2023-present  Gene C <arch@sapience.com>


