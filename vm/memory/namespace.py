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
# namespace MODULE
# --------------------------------------------------
"""
Variable namespace implementation
"""
# --------------------------------------------------
# imports
# --------------------------------------------------


# --------------------------------------------------
# namespace
# --------------------------------------------------
class Namespace:
    """
    Represents a variable namespace (locals or globals).
    """

    def __init__(self, parent=None):
        self._values = {}
        self._parent = parent
    
    def get(self, name: str):
        """
        Retrieve a variable value.
        """
        if name in self._values:
            return self._values[name]
        
        if self._parent is not None:
            return self._parent.get(name)
        
        raise KeyError(f"Variable not found: {name}")
    
    def set(self, name: str, value):
        """
        Set a variable value.
        """
        self._values[name] = value
    
    def exists(self, name: str) -> bool:
        """
        Check if variable exists in this namespace chain.
        """
        if name in self._values:
            return True
        
        if self._parent is not None:
            return self._parent.exists(name)
        
        return False
