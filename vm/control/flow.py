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
# flow MODULE
# --------------------------------------------------
"""
Control flow operations.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
from vm.errors import RuntimeExecutionError


# --------------------------------------------------
# control flow
# --------------------------------------------------
class ControlFlow:
    """
    Handles jump and branching logic.
    """

    @staticmethod
    def jump(frame, target: int):
        """
        Perform an unconditional jump.
        """
        if target < 0 or target >= len(frame.instructions):
            raise RuntimeExecutionError(
                f"Invalid jump target: {target}"
            )
        
        frame.jump(target)
    
    @staticmethod
    def jump_if_true(frame, condition, target: int):
        """
        Jump if condition evaluates to True.
        """
        if condition:
            ControlFlow.jump(frame, target)
    
    @staticmethod
    def jump_if_false(frame, condition, target: int):
        """
        Jump if condition evaluates to False.
        """
        if not condition:
            ControlFlow.jump(frame, target)
