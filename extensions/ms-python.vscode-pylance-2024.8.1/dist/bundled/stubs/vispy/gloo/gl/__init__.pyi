# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

# NOTE: modules in this package that start with one underscore are
# autogenerated, and should not be edited.

from __future__ import division as division

import os as os

from ...util import config as config, logger as logger
from ._constants import *  # noqa
from ._proxy import BaseGLProxy as BaseGLProxy

# Variable that will hold the module corresponding to the current backend
# This variable is used in our proxy classes to call the right functions.
current_backend: None = ...

class MainProxy(BaseGLProxy):
    def __call__(self, funcname, returns, *args): ...

# Instantiate proxy objects
proxy = ...

def use_gl(target: str | None = None): ...
def _clear_namespace(): ...
def _copy_gl_functions(source, dest, constants=False, debug=False): ...
def _arg_repr(arg): ...
def make_debug_wrapper(fn): ...
def check_error(when: str = "periodic check"): ...
def _fix_osmesa_gl_lib_if_testing(): ...

# Load default gl backend
from . import gl2 as default_backend  # noqa
