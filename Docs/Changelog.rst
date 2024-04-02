Changelog
=========

**[2.4.0] ----- 2024-04-02** ::

	    Fix passlib bcrrypt warning when can happen if python-bcyrpt is used.
	        The python bcrypt module is optional for passlib.
	        Fixes https://github.com/gene-git/nginx_passwd/issues/2 brought by @solsticedhiver
	    update Docs/Changelog.rst


**[2.3.1] ----- 2024-02-04** ::

	    tweak readme
	    update Docs/Changelog.rst


**[2.3.0] ----- 2024-02-04** ::

	    Add support for argon2,pbkdf2_sha512  and pbkdf2_sha256
	    Optional depends python-argon2_cffi for argon2 support
	    update Docs/Changelog.rst


**[2.2.0] ----- 2023-11-27** ::

	    Change python backend from poetry to hatch
	    update Docs/Changelog.rst


**[2.1.0] ----- 2023-09-27** ::

	    Reorganize documents and migrate to restructured text
	    update CHANGELOG.md


**[2.0.3] ----- 2023-09-20** ::

	    Small README tidy ups
	    update CHANGELOG.md


**[2.0.2] ----- 2023-09-18** ::

	    Fix typo in PKGBUILD file
	    update CHANGELOG.md


**[2.0.1] ----- 2023-09-18** ::

	    Change hashing code. Remove openssl and use python passlib.
	    Default algo is sha256
	    update CHANGELOG.md


**[1.1.0] ----- 2023-05-18** ::

	    install: switch from pip to python installer package. This adds optimized bytecode
	    update CHANGELOG.md


**[1.0.2] ----- 2023-05-18** ::

	    PKGBUILD: build wheel back to using python -m build instead of poetry
	    update CHANGELOG.md


**[1.0.1] ----- 2023-05-17** ::

	    Simplify Arch PKGBUILD and more closely follow arch guidelines
	    small readme chg
	    typo
	    tweak readme
	    update CHANGELOG.md


**[1.0.0] ----- 2023-04-17** ::

	    Add --verify to check password
	    update CHANGELOG.md


**[0.9.0] ----- 2023-04-17** ::

	    Initial Commit


