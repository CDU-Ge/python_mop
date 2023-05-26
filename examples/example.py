# -*- coding: utf-8 -*-
# Copyright (c) CDU

"""Model Docstrings

"""

from __future__ import absolute_import
from __future__ import annotations
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import mop


@mop.monitor(lambda v: 4 < v < 6, lambda v: 5)
def add0(a, b):
    return a + b


print(add0(1.1, 1.1))


@mop.monitor(int, int)
def add1(a, b):
    return a + b


print(add1(1.1, 1.1))


# 2

@mop.monitor(mop.mrv() == 1, None, 1)
def add2(a, b):
    return a + b


print(add2(1.1, 1.1))
# 1
