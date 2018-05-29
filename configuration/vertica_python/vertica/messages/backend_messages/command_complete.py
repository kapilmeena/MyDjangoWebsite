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

import re

from struct import unpack

from ..message import BackendMessage


class CommandComplete(BackendMessage):
    message_id = b'C'

    def __init__(self, data):
        BackendMessage.__init__(self)
        data = unpack('{0}sx'.format(len(data) - 1), data)[0]

        if re.match(b"INSERT", data) is not None:
            splitstr = data.split(b' ', 3)
            self.tag = splitstr[0]
            if len(splitstr) >= 2:
                self.oid = int(splitstr[1])
            if len(splitstr) >= 3:
                self.rows = int(splitstr[2])
        elif re.match(b"(DELETE|UPDATE|MOVE|FETCH|COPY)", data) is not None:
            splitstr = data.split(b' ', 2)
            self.tag = splitstr[0]
            if len(splitstr) >= 2:
                self.rows = int(splitstr[1])
        else:
            self.tag = data


BackendMessage.register(CommandComplete)