# Copyright (c) 2013-2017 Uber Technologies, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from __future__ import print_function, division, absolute_import

from .vertica.connection import Connection, connect

# Importing exceptions for compatibility with dbapi 2.0.
# See: PEP 249 - Python Database API 2.0
#      https://www.python.org/dev/peps/pep-0249/#exceptions
from . import errors
from .errors import (
    Error, Warning, DataError, DatabaseError, IntegrityError, InterfaceError,
    InternalError, NotSupportedError, OperationalError, ProgrammingError)

# Main module for this library.
__author__ = 'Uber Technologies, Inc'
__copyright__ = 'Copyright 2013, Uber Technologies, Inc.'
__license__ = 'MIT'

__all__ = ['Connection', 'PROTOCOL_VERSION', 'version_info', 'apilevel', 'threadsafety',
           'paramstyle', 'connect', 'Error', 'Warning', 'DataError', 'DatabaseError',
           'IntegrityError', 'InterfaceError', 'InternalError', 'NotSupportedError',
           'OperationalError', 'ProgrammingError']

# The version number of this library.
version_info = (0, 7, 3)
__version__ = '.'.join(map(str, version_info))

# The protocol version (3.0.0) implemented in this library.
PROTOCOL_VERSION = 3 << 16

apilevel = 2.0
threadsafety = 1  # Threads may share the module, but not connections!
paramstyle = 'named'  # WHERE name=:name