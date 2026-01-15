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
# disassembler MODULE
# --------------------------------------------------
"""
Bytecode Disassembler.

Converts VM bytecode into a readable, annotated format.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
from typing import List, Tuple


# --------------------------------------------------
# disassembler
# --------------------------------------------------
class Disassembler:
    """
    Disassembles parsed bytecode instructions.
    """

    def disassemble(self, instructions: List[Tuple[str, list]]
                    ) -> str:
        """
        Convert parsed instructions into readable text.
        """
        lines = []

        for index, (opcode, operands) in enumerate(instructions):
            operand_str = " ".join(operands)
            line = f"{index:04d}  {opcode}"

            if operand_str:
                line += f" {operand_str}"
            
            lines.append(line)
        
        return "\n".join(lines)
    
    def disassemble_file(self, path: str, loader, parser) -> str:
        """
        Load and disassemble a bytecode file.
        """
        raw = loader.load_from_file(path)
        instructions = parser.parse(raw)
        return self.disassemble(instructions)
