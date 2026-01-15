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
# constants MODULE
# --------------------------------------------------
"""
Constants pool.

Stores immutable constants used by bytecode.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------


# --------------------------------------------------
# constants pool
# --------------------------------------------------
class ConstantsPool:
    """
    Manages constants referenced by bytecode.
    """

    def __init__(self):
        self._constants = []
    
    def add(self, value):
        """
        Add a constant and return its index.
        """
        self._constants.append(value)
        return len(self._constants) - 1
    
    def get(self, index: int):
        """
        Retrieve a constant by index.
        """
        try:
            return self._constants[index]
        except IndexError:
            raise IndexError(f"Invalid constant index: {index}")
    
    def __len__(self):
        return len(self._constants)
