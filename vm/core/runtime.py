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
# runtime MODULE
# --------------------------------------------------
"""
Runtime coordination.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
from vm.control import CallStack
from vm.core.engine import ExecutionEngine


# --------------------------------------------------
# runtime
# --------------------------------------------------
class Runtime:
    """
    Coordinates execution engine and call stack
    """

    def __init__(self):
        self.callstack = CallStack()
        self.engine = ExecutionEngine()
    
    def run(self, frame):
        """
        Start execution with an initial frame.
        """
        self.callstack.push(frame)
        self.engine.execute(frame, self.callstack)
