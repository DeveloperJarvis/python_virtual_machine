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
# loader MODULE
# --------------------------------------------------
"""
Bytecode Loader.

Responsible for loading raw bytecode from a source.
The loader does not interpret instructions; it only
reads and normalizes input for the parser.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
import os
from typing import List


# --------------------------------------------------
# bytecode loader
# --------------------------------------------------
class BytecodeLoader:
    """
    Loads bytecode from filles or in-memory sources.
    """

    def load_from_file(self, path: str) -> List[str]:
        """
        Load bytecode instructions from a file.

        Each non-empty, non-comment line is treated as
        a single instruction.
        """
        if "\n" in path or not os.path.exists(path):
            return self.load_from_string(path)
        
        instructions = []

        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                # Ignore empty lines and comments
                if not line or line.startswith("#"):
                    continue

                instructions.append(line)
        
        return instructions
    
    def load_from_string(self, source: str) -> List[str]:
        """
        Load bytecode instructions from a string.
        """
        instructions = []

        for line in source.splitlines():
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            instructions.append(line)

        return instructions
