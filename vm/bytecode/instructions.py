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
# instructions MODULE
# --------------------------------------------------
"""
Instructions definitions for the Python Virtual Machine.

This module defines all supported opcodes and provides
metadata used by the parser and execution engine.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
from typing import Dict, Callable, List, Optional


# --------------------------------------------------
# instruction
# --------------------------------------------------
class Instruction:
    """
    Represents a single VM instruction.
    """

    def __init__(
            self,
            name: str,
            operand_count: int = 0,
            description: Optional[str] = None,
        ):
        self.name = name
        self.operand_count = operand_count
        self.description = description or ""
    
    def __repr__(self) -> str:
        return (f"Instruction(name={self.name}, "
                f"operands={self.operand_count})")


# --------------------------------------------------
# opcode registry
# --------------------------------------------------
INSTRUCTION_SET: Dict[str, Instruction] = {
    # Data operations
    "LOAD_CONST": Instruction(
        name="LOAD_CONST",
        operand_count=1,
        description="Push constant onto the operand stack",
    ),
    "LOAD_VAR": Instruction(
        name="LOAD_VAR",
        operand_count=1,
        description="Load operand value onto the stack",
    ),
    "STORE_VAR": Instruction(
        name="STORE_VAR",
        operand_count=1,
        description="Store top of stack into variable",
    ),

    # Arithmetic operations
    "ADD": Instruction(
        name="ADD",
        description="Add top two values on the stack",
    ),
    "SUB": Instruction(
        name="SUB",
        description="Subtract top two values on the stack",
    ),
    "MUL": Instruction(
        name="MUL",
        description="Multiply top two values on the stack",
    ),
    "DIV": Instruction(
        name="DIV",
        description="Divide top two values on the stack",
    ),

    # Stack manipulation
    "POP_TOP": Instruction(
        name="POP_TOP",
        description="Remove top of stack",
    ),
    "DUP_TOP": Instruction(
        name="DUP_TOP",
        description="Duplicate top of stack",
    ),

    # Control flow
    "JUMP": Instruction(
        name="JUMP",
        operand_count=1,
        description="Unconditional jump",
    ),
    "JUMP_IF_TRUE": Instruction(
        name="JUMP_IF_TRUE",
        operand_count=1,
        description="Jump if condition is true",
    ),
    "JUMP_IF_FALSE": Instruction(
        name="JUMP_IF_FALSE",
        operand_count=1,
        description="Jump if condition is false",
    ),

    # Function calls
    "CALL_FUNC": Instruction(
        name="CALL_FUNC",
        operand_count=1,
        description="Call function with N argumnets",
    ),
    "RETURN_VAL": Instruction(
        name="RETURN_VAL",
        description="Return value from function",
    ),

    # Program control
    "HALT": Instruction(
        name="HALT",
        description="Stop VM execution",
    ),
}

# Public opcode loopup (used by parser)
OPCODES = set(INSTRUCTION_SET.keys())

def get_instruction(name: str) -> Instruction:
    """
    Retrieve instruction metadata by opcode name.
    """
    return INSTRUCTION_SET[name]
