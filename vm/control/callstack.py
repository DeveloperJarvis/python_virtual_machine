# --------------------------------------------------
# -*- Python -*- Compatibility Header
#
# Copyright (C) 2023 Developer Jarvis (Pen Name)
#
# This file is part of the Python Virtual Machine Library. This library is free
# software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Python Virtual Machine - Parse bytecode and execute instructions (custom VM)
#                       Skills: parsing, bytecode, stack machines, interpreters
#
# Author: Developer Jarvis (Pen Name)
# Contact: https://github.com/DeveloperJarvis
#
# --------------------------------------------------

# --------------------------------------------------
# callstack MODULE
# --------------------------------------------------
"""
Call stack implementation.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
from config.config import MAX_CALL_DEPTH
from vm.errors import CallStackOverflowError


# --------------------------------------------------
# call stack
# --------------------------------------------------
class CallStack:
    """
    Manages execution frames.
    """

    def __init__(self):
        self._frames = []
    
    def push(self, frame):
        """
        Push a new frame onto the call stack.
        """
        if len(self._frames) >= MAX_CALL_DEPTH:
            raise CallStackOverflowError(
                "Maximum call stack depth exceeded"
            )
        
        self._frames.append(frame)
    
    def pop(self):
        """
        Pop the current frame.
        """
        return self._frames.pop()
    
    def current(self):
        """
        Get the current frame.
        """
        if not self._frames:
            return None
        
        return self._frames[-1]
    
    def is_empty(self) -> bool:
        return not self._frames
