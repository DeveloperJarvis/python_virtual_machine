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
# exceptions MODULE
# --------------------------------------------------
"""
Custom exceptions for the Python Virtual Machine.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------


# --------------------------------------------------
# vm error
# --------------------------------------------------
class VMError(Exception):
    """
    Base class for all VM-related errors.
    """


# --------------------------------------------------
# bytecode & parsing errors
# --------------------------------------------------
class BytecodeError(VMError):
    """
    Raised when bytecode is malformed or invalid.
    """
    pass


class InvalidOpcodeError(BytecodeError):
    """
    Raised when an unknown or unsupported opcode is encountered.
    """
    def __init__(self, opcode: str):
        super().__init__(f"Invalid opcode: {opcode}")
        self.opcode = opcode


# --------------------------------------------------
# stack errors
# --------------------------------------------------
class StackUnderflowError(VMError):
    """
    Raised when popping from an empty operand stack.
    """
    pass


class StackOverflowError(VMError):
    """
    Raised when the operand stack exceeds its maximum size.
    """
    pass


# --------------------------------------------------
# runtime errors
# --------------------------------------------------
class RuntimeExecutionError(VMError):
    """
    Raised when a runtime execution error occurs.
    """
    pass


class VariableNotFoundError(RuntimeExecutionError):
    """
    Raised when accessing an undefined variable.
    """
    def __init__(self, name: str):
        super().__init__(f"Variable not found: {name}")
        self.name = name


class CallStackOverflowError(RuntimeExecutionError):
    """
    Raised when the call stack exceeds its maximum depth.
    """
    pass
