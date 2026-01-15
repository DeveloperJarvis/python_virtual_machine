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
# assembler MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
from typing import List

from vm.bytecode.instructions import OPCODES
from vm.errors import BytecodeError


# --------------------------------------------------
# assembler
# --------------------------------------------------
class Assembler:
    """
    Assmbles human-readable instructions into bytecode.
    """

    def assemble(self, source: str) -> List[str]:
        """
        Convert assembly source into bytecode lines.
        """
        bytecode = []

        for lineno, line in enumerate(source.splitlines(),
                                      start=1):
            line = line.strip()

            # Ignore comments and empty lines
            if not line or line.startswith("#"):
                continue

            parts = line.split()
            opcode = parts[0]
            operands = parts[1:]

            if opcode not in OPCODES:
                raise BytecodeError(
                    f"Unknown opcode '{opcode}' at line {lineno}"
                )
            
            # Normalize spacing
            bytecode.append(" ".join([opcode, *operands]))
        
        return bytecode

    def assemble_file(self, input_path: str, output_path: str):
        """
        Assemble source file into a bytecode file.
        """
        with open(input_path, "r", encoding="utf-8") as src:
            source = src.read()
        
        bytecode = self.assemble(source)

        with open(output_path, "w", encoding="utf-8") as out:
            for line in bytecode:
                out.write(line + "\n")
