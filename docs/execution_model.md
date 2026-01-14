# Execution Model

## Python Virtual Machine – Runtime & Execution Semantics

This document describes **how bytecode is executed** by the Python Virtual Machine, focusing on the **runtime model**, **stack behavior**, **frames**, and the **instruction execution lifecycle**.

The VM follows a **stack-based execution model** inspired by CPython, while remaining intentionally minimal and explicit.

---

## 1. Core Execution Loop

The VM executes bytecode using a classic **fetch–decode–execute** cycle.

### Execution Steps

1. Fetch instruction at the current Instruction Pointer (IP)
2. Decode opcode and operands
3. Execute instruction logic
4. Update IP
5. Repeat until `HALT`

This loop continues until:

- A `HALT` instruction is encountered
- A fatal runtime error occurs

---

## 2. Instruction Pointer (IP)

- Each execution frame owns its own IP
- IP always points to the next instruction to execute
- Default behavior increments IP by 1
- Control-flow instructions explicitly modify IP

This design enables:

- Loops
- Conditionals
- Function calls

---

## 3. Operand Stack

The operand stack is central to execution.

### Responsibilities

- Hold intermediate computation values
- Pass arguments to functions
- Store return values

### Stack Rules

- Instructions pop required operands
- Results are pushed back
- Stack underflow results in a runtime error
- Stack overflow is guarded by configurable limits

---

## 4. Execution Frames

Each function call creates a **new execution frame**.

### Frame Contents

- Instruction Pointer (IP)
- Operand stack
- Local variable namespace
- Reference to parent frame

### Frame Lifecycle

1. Frame is created on function call
2. Execution switches to new frame
3. Frame executes until return
4. Frame is destroyed
5. Execution resumes in caller frame

---

## 5. Call Stack

The VM maintains a **call stack** of frames.

- Top frame = currently executing context
- Supports nested calls and recursion
- Maximum depth is configurable

Errors occur if call depth exceeds limits.

---

## 6. Variable Resolution

### Variable Scopes

1. Local (current frame)
2. Global (shared namespace)

Resolution order:

- Check local scope
- Fallback to global scope
- Raise error if unresolved (unless explicitly allowed)

---

## 7. Function Call Execution

### Call Sequence

1. Push function arguments onto stack
2. `CALL_FUNC` instruction:

   - Pops arguments
   - Creates new frame
   - Transfers control

3. Function executes
4. `RETURN_VAL`:

   - Pops return value
   - Restores caller frame
   - Pushes return value onto caller stack

---

## 8. Control Flow

### Conditional Execution

- Condition value is popped from stack
- Truthiness determines jump behavior
- IP is updated accordingly

### Loops

- Implemented using conditional and unconditional jumps
- Loop state maintained entirely via IP manipulation

---

## 9. Error Handling

### Runtime Errors

- Stack underflow / overflow
- Invalid opcode
- Invalid jump target
- Division by zero
- Undefined variable access

### Error Strategy

- Execution halts on fatal error
- VM raises a structured exception
- Execution state may be logged for debugging

---

## 10. Program Termination

Execution ends when:

- `HALT` instruction is executed
- An unhandled runtime error occurs

Upon termination:

- All frames are discarded
- Final stack state may be returned or logged

---

## 11. Debug & Tracing Support

Optional debugging features include:

- Instruction tracing
- Stack state snapshots
- Frame inspection

These features are configurable and disabled by default.

---

## 12. Design Constraints

- No JIT compilation
- No garbage collection
- No native extensions
- Deterministic execution

---

## 13. Summary

This execution model defines a clear, deterministic runtime for executing bytecode using a stack-based virtual machine. The explicit handling of frames, stacks, and instruction flow makes the VM easy to reason about, extend, and debug.
