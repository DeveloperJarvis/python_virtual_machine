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
# test_bytecode MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import pytest

from vm.bytecode import BytecodeLoader, BytecodeParser
from vm.errors import BytecodeError


def test_bytecode_loader_from_string():
    source = """
        LOAD_CONST 10
        LOAD_CONST 20
        ADD
    """
    loader = BytecodeLoader()
    result = loader.load_from_file(source)

    assert result == [
        "LOAD_CONST 10",
        "LOAD_CONST 20",
        "ADD",
    ]


def test_bytecode_parser_valid():
    raw = [
        "LOAD_CONST 5",
        "LOAD_CONST 6",
        "ADD",
    ]
    parser = BytecodeParser()
    parsed = parser.parse(raw)

    assert parsed[0] == ("LOAD_CONST", ["5"])
    assert parsed[1] == ("LOAD_CONST", ["6"])
    assert parsed[2] == ("ADD", [])


def test_bytecode_parser_invalid_opcode():
    raw = ["INVALID_OP 123"]
    parser = BytecodeParser()
    
    with pytest.raises(ValueError):
        parser.parse(raw)
