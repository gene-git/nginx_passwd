# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2022-present  Gene C <arch@sapience.com>
"""
nginx-passwd class
"""
# pylint: disable=too-few-public-methods
from typing import (Dict)

from .class_ngpopts import NgpOpts


class NgpBase:
    """
    nginx-passwd manager base class

    Base class holds data - child class has methods.
    """
    def __init__(self):

        self.okay: bool = True
        self.opts: NgpOpts = NgpOpts()
        self.passwd_data: Dict[str, str] = {}
        self.passwd_item: str = ''
