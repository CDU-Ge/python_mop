# -*- coding: utf-8 -*-
# Copyright (c) CDU

"""Model Docstrings

"""

from __future__ import absolute_import
from __future__ import annotations
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import inspect


def example(a, *args, b=None, **kwargs) -> None:
    return None


if __name__ == '__main__':
    sig = inspect.signature(example)
    print(sig)
    print(sig.parameters)
