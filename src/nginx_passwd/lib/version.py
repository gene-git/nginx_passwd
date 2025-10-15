# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2022-present  Gene C <arch@sapience.com>
"""
Project nginx_passwd
"""
__version__ = "3.0.1"
__date__ = "2025-10-15"
__reldev__ = "release"


def version() -> str:
    """ report version and release date """
    vers = f'wg-tool: version {__version__} ({__reldev__}, {__date__})'
    return vers
