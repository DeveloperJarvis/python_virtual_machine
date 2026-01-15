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
# engine MODULE
# --------------------------------------------------
"""
Instruction execution engine.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
from vm.bytecode.instructions import get_instruction
from vm.control import ControlFlow
from vm.errors import (
    InvalidOpcodeError,
    RuntimeExecutionError,
)
from vm.utils import debug_log, trace_instruction


# --------------------------------------------------
# execution engine
# --------------------------------------------------
class ExecutionEngine:
    """
    Executes parsed instructions within a frame.
    """

    def execute(self, frame, callstack):
        """
        Execute instructions until frame completes.
        """
        while True:
            instr = frame.next_instruction()

            if instr is None:
                return
            
            opcode, operands = instr
            trace_instruction(frame.ip - 1, opcode, operands,
                              frame.stack)
            
            try:
                self.dispatch(opcode, operands, frame,
                              callstack)
            except Exception as exc:
                raise RuntimeExecutionError(str(exc)) from exc
    
    def dispatch(self, opcode, operands, frame, callstack):
        """
        Dispatch opcode to handler.
        """
        handler_name = f"op_{opcode.lower()}"

        if not hasattr(self, handler_name):
            raise InvalidOpcodeError(opcode)
        
        handler = getattr(self, handler_name)
        handler(operands, frame, callstack)
    
    # -----------------------------------
    # opcode handlers
    # -----------------------------------

    def op_load_const(self, operands, frame, _):
        value = operands[0]
        frame.stack.push(self._parse_literal(value))
    
    def op_load_var(self, operands, frame, _):
        name = operands[0]
        frame.stack.push(frame.locals.get(name))

    def op_store_var(self, operands, frame, _):
        name = operands[0]
        value = frame.stack.pop()
        frame.locals.set(name, value)

    def op_add(self, _, frame, __):
        b = frame.stack.pop()
        a = frame.stack.pop()
        frame.stack.push(a + b)

    def op_sub(self, _, frame, __):
        b = frame.stack.pop()
        a = frame.stack.pop()
        frame.stack.push(a - b)
    
    def op_mul(self, _, frame, __):
        b = frame.stack.pop()
        a = frame.stack.pop()
        frame.stack.push(a * b)
    
    def op_div(self, _, frame, __):
        b = frame.stack.pop()
        a = frame.stack.pop()
        frame.stack.push(a / b)
    
    def op_jump(self, operands, frame, __):
        ControlFlow.jump(frame, int(operands[0]))
    
    def op_jump_if_true(self, operands, frame, __):
        condition = frame.stack.pop()
        ControlFlow.jump_if_true(frame, condition,
                                 int(operands[0]))
    
    def op_jump_if_false(self, operands, frame, __):
        condition = frame.stack.pop()
        ControlFlow.jump_if_false(frame, condition,
                                  int(operands[0]))
    
    def op_pop_top(self, _, frame, __):
        frame.stack.pop()
    
    def op_dup_top(self, _, frame, __):
        value = frame.stack.peek()
        frame.stack.push(value)
    
    def op_return_val(self, _, frame, callstack):
        value = frame.stack.pop()
        callstack.pop()
        caller = callstack.current()

        if caller:
            caller.stack.push(value)
        
    def op_halt(self, _, frame, callstack):
        callstack.pop()
    
    def op_call_func(self, operands, frame, _):
        """
        Call a Python callable stored on the stack.
        CALL_FUNC <arg_count>
        Stack before:   [..., func, arg1, arg2, ..., argN]
        Stack after:    [..., result]
        """
        arg_count = int(operands[0])

        # Pop arguments (reverse order)
        args = []
        for _ in range(arg_count):
            args.append(frame.stack.pop())
        args.reverse()

        # Pop function
        func = frame.stack.pop()

        if not callable(func):
            raise RuntimeExecutionError("Object is not callable")
        
        result = func(*args)
        frame.stack.push(result)

    # -----------------------------------
    # helpers
    # -----------------------------------

    def _parse_literal(self, value: str):
        """
        Convert literal string to Python value.
        """
        if value.isdigit():
            return int(value)
        try:
            return float(value)
        except ValueError:
            return value.strip('"')
