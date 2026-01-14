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
# config MODULE
# --------------------------------------------------
"""
Global configuration settings for the Python Virtual Machine.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
import os


# --------------------------------------------------
# debug & logging
# --------------------------------------------------
# Enable debug mode
DEBUG = False
# Trace each instruction during execution
TRACE_EXECUTION = False
# logging file
PROJECT_DIR = os.path.join(os.path.abspath(__file__), "..")
LOG_FILE = os.path.join(PROJECT_DIR, "logs", "vm.log")


# --------------------------------------------------
# runtime limits
# --------------------------------------------------
# Maximum size of the operand stack
MAX_STACK_SIZE = 1024
# Maximum depth of the call stack
MAX_CALL_DEPTH = 256


# --------------------------------------------------
# VM behaviour flags
# --------------------------------------------------
# Halt execution on first runtime error
HALT_ON_ERROR = True
# Allow undefined variable access (for experimentation)
ALLOW_UNDEFINED_VARS = False
