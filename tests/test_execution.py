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
# test_execution MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
from vm.core.vm import VirtualMachine


def test_simple_arithmetic_execution():
    vm = VirtualMachine()

    source = """
        LOAD_CONST 2
        LOAD_CONST 3
        ADD
        STORE_VAR result
        HALT
    """

    vm.run_string(source)

    assert vm.globals.get("result") == 5


def test_variable_assignment():
    vm = VirtualMachine()

    source = """
        LOAD_CONST 10
        STORE_VAR x
        LOAD_VAR x
        LOAD_CONST 5
        MUL
        STORE_VAR y
        HALT
    """

    vm.run_string(source)

    assert vm.globals.get("x") == 10
    assert vm.globals.get("y") == 50
