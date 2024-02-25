# -*- coding: utf-8 -*-
# Copyright (c) CDU

"""overload


"""

from __future__ import absolute_import
from __future__ import annotations
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import types
import inspect


class CallFunction:
    def __init__(self, func: types.FunctionType):
        self.name = func.__name__
        self.__doc__ = func.__doc__ or ""
        self.func = func

        self._call_tables = {"default": func}

    def register(self, func: types.FunctionType) -> 'CallFunction':
        sig = inspect.signature(func)
        for (n, p) in sig.parameters.items():
            p: inspect.Parameter
            print(n, p.name, p.kind, p.annotation, p.default)
        print(inspect.getsource(func))
        self._call_tables[f'{len(sig.parameters)}'] = func
        self.__doc__ += func.__doc__ or ""
        self.func.__doc__ = self.__doc__
        return self

    def __call__(self, *args, **kwargs):
        index = len(args) + min(len(kwargs.keys()), 1)
        func = self._call_tables.get(f"{index}", self._call_tables['default'])

        print(inspect.getsource(func))
        return func(*args, **kwargs)


def overload(func: types.FunctionType) -> CallFunction:
    """
    依据参数数量进行重载

    :param func:
    :return:
    """
    return CallFunction(func)


if __name__ == '__main__':
    ...