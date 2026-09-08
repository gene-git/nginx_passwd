Changelog
=========

Tags
====

.. code-block:: text

	0.9.0 (2023-04-17) -> 4.0.0 (2026-09-08)
	63 commits.

Commits
=======


* 2026-09-08  : **4.0.0**

.. code-block:: text

              - **Version 4.0.0**
            
                * Default hash algo is argon2
                * Use meson / meson python for build and package management
                * Periodic code review
                * tests use (and check depends) on pyconcurrent package.
 2026-05-05   ⋯

.. code-block:: text

              - update Docs/Changelogs

* 2026-05-05  : **3.3.2**

.. code-block:: text

              - Fix goofy typo in installer - thanks to @solsticedhiver in the aur
 2026-01-04   ⋯

.. code-block:: text

              - update Docs/Changelogs

* 2026-01-04  : **3.3.1**

.. code-block:: text

              - Small non-code tidy ups
              - update Docs/Changelogs

* 2026-01-04  : **3.3.0**

.. code-block:: text

                  - **Version 3.3.0**
            
                    * Source code reorg
                    * Switch python packager from hatch to uv
                    * Confirm all working with python 3.14.2
 2025-12-22   ⋯

.. code-block:: text

              - update Docs/Changelogs Docs/${my_name}.pdf

* 2025-12-22  : **3.2.1**

.. code-block:: text

              - Installer: use new path to license
              - update Docs/Changelogs Docs/${my_name}.pdf

* 2025-12-22  : **3.2.0**

.. code-block:: text

              - * Little doc cleanups

* 2025-12-22  : **3.1.0**

.. code-block:: text

              - * Remove os.getlogin() in tests (ENOTTY reported by @ccharabaruk on AUR package).
                * Small tidy ups
 2025-10-15   ⋯

.. code-block:: text

              - update Docs/Changelogs Docs/${my_name}.pdf

* 2025-10-15  : **3.0.1**

.. code-block:: text

              - **Version 3.0.0**
            
                * Reduce our reliance on passlib (it is unmaintained).
            
                  * passlib bcrypt is broken
                  * there is a fork which works
            
                * Algo changes no longer using passlib:
            
                  * bcrypt now uses python-bcrypt directly
                  * argon2 now uses python-argon2-cffi (which uses C library)
                  * pbkdf2_sha512 now uses python-cryptography
                  * pbkdf2_sha256 now uses python-cryptography
            
                * Switch license to GPL-2.0-or-later
            
                * Allow algo names to be hypen or underscore (pbkdf2-sha256 or pbkdf2_sha256)
 2025-05-21   ⋯

.. code-block:: text

              - update Docs/Changelogs Docs/${my_name}.pdf

* 2025-05-21  : **2.8.0**

.. code-block:: text

              - Use builtin types where possible. e.g. typing.List -> list
 2025-05-19   ⋯

.. code-block:: text

              - update Docs/Changelogs Docs/${my_name}.pdf

* 2025-05-19  : **2.7.3**

.. code-block:: text

              - Arch PKGBUILD: move pytest dependency to checkdepends from makedepends
 2025-05-15   ⋯

.. code-block:: text

              - update Docs/Changelogs Docs/${my_name}.pdf

* 2025-05-15  : **2.7.2**

.. code-block:: text

              - typo
              - update Docs/Changelogs Docs/${my_name}.pdf

* 2025-05-15  : **2.7.1**

.. code-block:: text

              - Add missing PKGBUILD dependencies so pytest does not fail
                  Fixes issue #5 thanks to @SoLoR1
 2025-05-14   ⋯

.. code-block:: text

              - update Docs/Changelogs Docs/${my_name}.pdf

* 2025-05-14  : **2.6.0**

.. code-block:: text

              - * PEP-8, PEP-257, PEP-484 and PEP 561
                * Refactor code
                * Add pytests
                * add python-bcrypt dependency to Arch PKBUILD
 2024-12-31   ⋯

.. code-block:: text

              - update Docs/Changelog.rst Docs/nginx_passwd.pdf

* 2024-12-31  : **2.5.2**

.. code-block:: text

              - Git tags are now signed.
                Update SPDX tags
                Add git signing key to Arch Package
                Bump python vers
 2024-10-13   ⋯

.. code-block:: text

              - update Docs/Changelog.rst Docs/nginx_passwd.pdf

* 2024-10-13  : **2.5.1**

.. code-block:: text

              - Minor readme update
 2024-04-04   ⋯

.. code-block:: text

              - update Docs/Changelog.rst Docs/nginx_passwd.pdf

* 2024-04-04  : **2.5.0**

.. code-block:: text

              - update Docs/Changelog.rst Docs/nginx_passwd.pdf
              - Fix bug deleting last entry in password file.
                      Thanks to solsticedhive for finding and providing patch.
                      Fixes https://github.com/gene-git/nginx_passwd/issues/3
                Bug : if no user given then it is set to "None".
                      Thanks to @olsticedhiver
                      Fixes https://github.com/gene-git/nginx_passwd/issues/4
 2024-04-02   ⋯

.. code-block:: text

              - update Docs/Changelog.rst Docs/nginx_passwd.pdf
              - tweak readme

* 2024-04-02  : **2.4.0**

.. code-block:: text

              - update Docs/Changelog.rst Docs/nginx_passwd.pdf
              - update Docs/Changelog.rst
              - Fix passlib bcrrypt warning when can happen if python-bcyrpt is used.
                    The python bcrypt module is optional for passlib.
                    Fixes https://github.com/gene-git/nginx_passwd/issues/2 brought by @solsticedhiver
 2024-02-04   ⋯

.. code-block:: text

              - update Docs/Changelog.rst

* 2024-02-04  : **2.3.1**

.. code-block:: text

              - tweak readme
              - update Docs/Changelog.rst

* 2024-02-04  : **2.3.0**

.. code-block:: text

              - Add support for argon2,pbkdf2_sha512  and pbkdf2_sha256
                Optional depends python-argon2_cffi for argon2 support
 2023-11-27   ⋯

.. code-block:: text

              - update Docs/Changelog.rst

* 2023-11-27  : **2.2.0**

.. code-block:: text

              - Change python backend from poetry to hatch
 2023-09-27   ⋯

.. code-block:: text

              - update Docs/Changelog.rst

* 2023-09-27  : **2.1.0**

.. code-block:: text

              - Reorganize documents and migrate to restructured text
 2023-09-20   ⋯

.. code-block:: text

              - update CHANGELOG.md

* 2023-09-20  : **2.0.3**

.. code-block:: text

              - Small README tidy ups
 2023-09-18   ⋯

.. code-block:: text

              - update CHANGELOG.md

* 2023-09-18  : **2.0.2**

.. code-block:: text

              - Fix typo in PKGBUILD file
              - update CHANGELOG.md

* 2023-09-18  : **2.0.1**

.. code-block:: text

              - Change hashing code. Remove openssl and use python passlib.
                Default algo is sha256
 2023-05-18   ⋯

.. code-block:: text

              - update CHANGELOG.md

* 2023-05-18  : **1.1.0**

.. code-block:: text

              - install: switch from pip to python installer package. This adds optimized bytecode
              - update CHANGELOG.md

* 2023-05-18  : **1.0.2**

.. code-block:: text

              - PKGBUILD: build wheel back to using python -m build instead of poetry
 2023-05-17   ⋯

.. code-block:: text

              - update CHANGELOG.md

* 2023-05-17  : **1.0.1**

.. code-block:: text

              - Simplify Arch PKGBUILD and more closely follow arch guidelines
 2023-04-17   ⋯

.. code-block:: text

              - small readme chg
              - typo
              - tweak readme
              - update CHANGELOG.md

* 2023-04-17  : **1.0.0**

.. code-block:: text

              - Add --verify to check password
              - update CHANGELOG.md

* 2023-04-17  : **0.9.0**

.. code-block:: text

              - Initial Commit


