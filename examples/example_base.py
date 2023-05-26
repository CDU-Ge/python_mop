# -*- coding: utf-8 -*-
# Copyright (c) CDU

"""Model Docstrings

"""

from __future__ import absolute_import
from __future__ import annotations
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from mop import monitor
from mop import mrv


@monitor(int, int)
def example_0(a, b):
    return a + b


@monitor(float, monitor(float, float)(int))
def example_1(a, b):
    return a + b


@monitor(mrv() == 1, None, 1)
def example_2(a, b):
    return a + b


@monitor(mrv() == 1, None, 1)
def example_2(a, b):
    return a / b


if __name__ == '__main__':
    from mop import logger as mop_logger
    mop_logger.logger.setLevel(logging.DEBUG)
    print(example_0(1.1, 1.1), type(example_0(1.1, 1.1)) == int)
    print(example_1(1.1, 1.1), type(example_1(1.1, 1.1)) == float)
    print(example_2(1.1, 1.1), example_2(1.1, 1.1) == 1)
    print(example_2(1.1, 0), example_2(1.1, 0) == 1)

