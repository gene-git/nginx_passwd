=========
Changelog
=========

Tags
====

::

	0.9.0 (2023-04-17) -> 2.7.3 (2025-05-19)
	46 commits.

Commits
=======


* 2025-05-19  : **2.7.3**

::

                Arch PKGBUILD: move pytest dependency to checkdepends from makedepends
 2025-05-15     update Docs/Changelogs Docs/${my_name}.pdf

* 2025-05-15  : **2.7.2**

::

                typo
                update Docs/Changelogs Docs/${my_name}.pdf

* 2025-05-15  : **2.7.1**

::

                Add missing PKGBUILD dependencies so pytest does not fail
                  Fixes issue #5 thanks to @SoLoR1
 2025-05-14     update Docs/Changelogs Docs/${my_name}.pdf

* 2025-05-14  : **2.6.0**

::

                * PEP-8, PEP-257, PEP-484 and PEP 561
                * Refactor code
                * Add pytests
                * add python-bcrypt dependency to Arch PKBUILD
 2024-12-31     update Docs/Changelog.rst Docs/nginx_passwd.pdf

* 2024-12-31  : **2.5.2**

::

                Git tags are now signed.
                Update SPDX tags
                Add git signing key to Arch Package
                Bump python vers
 2024-10-13     update Docs/Changelog.rst Docs/nginx_passwd.pdf

* 2024-10-13  : **2.5.1**

::

                Minor readme update
 2024-04-04     update Docs/Changelog.rst Docs/nginx_passwd.pdf

* 2024-04-04  : **2.5.0**

::

                update Docs/Changelog.rst Docs/nginx_passwd.pdf
                Fix bug deleting last entry in password file.
                      Thanks to solsticedhive for finding and providing patch.
                      Fixes https://github.com/gene-git/nginx_passwd/issues/3
                Bug : if no user given then it is set to "None".
                      Thanks to @olsticedhiver
                      Fixes https://github.com/gene-git/nginx_passwd/issues/4
 2024-04-02     update Docs/Changelog.rst Docs/nginx_passwd.pdf
                tweak readme

* 2024-04-02  : **2.4.0**

::

                update Docs/Changelog.rst Docs/nginx_passwd.pdf
                update Docs/Changelog.rst
                Fix passlib bcrrypt warning when can happen if python-bcyrpt is used.
                    The python bcrypt module is optional for passlib.
                    Fixes https://github.com/gene-git/nginx_passwd/issues/2 brought by
                    @solsticedhiver
 2024-02-04     update Docs/Changelog.rst

* 2024-02-04  : **2.3.1**

::

                tweak readme
                update Docs/Changelog.rst

* 2024-02-04  : **2.3.0**

::

                Add support for argon2,pbkdf2_sha512  and pbkdf2_sha256
                Optional depends python-argon2_cffi for argon2 support
 2023-11-27     update Docs/Changelog.rst

* 2023-11-27  : **2.2.0**

::

                Change python backend from poetry to hatch
 2023-09-27     update Docs/Changelog.rst

* 2023-09-27  : **2.1.0**

::

                Reorganize documents and migrate to restructured text
 2023-09-20     update CHANGELOG.md

* 2023-09-20  : **2.0.3**

::

                Small README tidy ups
 2023-09-18     update CHANGELOG.md

* 2023-09-18  : **2.0.2**

::

                Fix typo in PKGBUILD file
                update CHANGELOG.md

* 2023-09-18  : **2.0.1**

::

                Change hashing code. Remove openssl and use python passlib.
                Default algo is sha256
 2023-05-18     update CHANGELOG.md

* 2023-05-18  : **1.1.0**

::

                install: switch from pip to python installer package. This adds optimized
                bytecode
                update CHANGELOG.md

* 2023-05-18  : **1.0.2**

::

                PKGBUILD: build wheel back to using python -m build instead of poetry
 2023-05-17     update CHANGELOG.md

* 2023-05-17  : **1.0.1**

::

                Simplify Arch PKGBUILD and more closely follow arch guidelines
 2023-04-17     small readme chg
                typo
                tweak readme
                update CHANGELOG.md

* 2023-04-17  : **1.0.0**

::

                Add --verify to check password
                update CHANGELOG.md

* 2023-04-17  : **0.9.0**

::

                Initial Commit


