'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLX import _types as _cs
# End users want this...
from OpenGL.raw.GLX._types import *
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLX_EXT_fbconfig_packed_float'
def _f( function ):
    return _p.createFunction( function,_p.GLX,'GLX_EXT_fbconfig_packed_float')
GLX_RGBA_UNSIGNED_FLOAT_BIT_EXT=_C('GLX_RGBA_UNSIGNED_FLOAT_BIT_EXT',0x00000008)
GLX_RGBA_UNSIGNED_FLOAT_TYPE_EXT=_C('GLX_RGBA_UNSIGNED_FLOAT_TYPE_EXT',0x20B1)
