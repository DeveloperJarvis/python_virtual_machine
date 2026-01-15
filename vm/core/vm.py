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
# vm MODULE
# --------------------------------------------------
"""
Top-level Virtual Machine interface.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
from vm.bytecode import BytecodeLoader, BytecodeParser
from vm.core.runtime import Runtime
from vm.memory import Namespace
from vm.stack import Frame
from vm.utils import debug_log


# --------------------------------------------------
# virtual machine
# --------------------------------------------------
class VirtualMachine:
    """
    Python Virtual Machine.
    """

    def __init__(self):
        self.loader = BytecodeLoader()
        self.parser = BytecodeParser()
        self.runtime = Runtime()
        self.globals = Namespace()
    
    def run_file(self, path: str):
        """
        Execute bytecode from file.
        """
        debug_log(f"Loading bytecode from {path}")
        raw = self.loader.load_from_file(path)
        instructions = self.parser.parse(raw)
        frame = Frame(instructions, self.globals,
                      locals_ns=self.globals)
        self.runtime.run(frame)
    
    def run_string(self, source: str):
        """
        Execute bytecode from string.
        """
        raw = self.loader.load_from_string(source)
        instructions = self.parser.parse(raw)
        frame = Frame(instructions, self.globals,
                      locals_ns=self.globals)
        self.runtime.run(frame)
