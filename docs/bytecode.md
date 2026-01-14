# Bytecode Specification

## Python Virtual Machine – Bytecode Format

This document defines the **bytecode format**, **instruction layout**, and **execution semantics** for the custom Python Virtual Machine (VM).

The bytecode is designed to be:

- Simple
- Stack-based
- Human-readable (optionally)
- Easy to parse and extend

---

## 1. Design Principles

- **Stack-based execution**
  All operations consume and produce values via the operand stack.

- **Linear instruction stream**
  Bytecode is executed sequentially unless control-flow instructions modify the instruction pointer.

- **Minimal instruction set**
  Only core operations required for computation and control flow are included.

- **Explicit operands**
  Instructions may include zero or more operands.

---

## 2. Bytecode Structure

Bytecode is represented as an **ordered list of instructions**.

Each instruction consists of:

- **Opcode** – Operation identifier
- **Operand(s)** – Optional arguments

### Conceptual Format

```
<OPCODE> [OPERAND_1] [OPERAND_2]
```

### Example

```
LOAD_CONST 10
LOAD_CONST 20
ADD
STORE_VAR x
```

---

## 3. Instruction Pointer (IP)

- The VM maintains an **Instruction Pointer (IP)**
- IP always points to the currently executing instruction
- After execution, IP increments by default
- Control-flow instructions may override IP

---

## 4. Operand Stack

The operand stack is used to:

- Store intermediate values
- Pass arguments to functions
- Hold return values

### Stack Rules

- Instructions **pop operands** from the stack
- Results are **pushed back** onto the stack
- Stack underflow results in a runtime error

---

## 5. Instruction Categories

### 5.1 Data Instructions

| Opcode       | Description                        |
| ------------ | ---------------------------------- |
| `LOAD_CONST` | Push a constant onto the stack     |
| `LOAD_VAR`   | Push variable value onto the stack |
| `STORE_VAR`  | Pop value and store in variable    |

---

### 5.2 Arithmetic Instructions

| Opcode | Stack Effect  |
| ------ | ------------- |
| `ADD`  | a, b → a + b  |
| `SUB`  | a, b → a - b  |
| `MUL`  | a, b → a \* b |
| `DIV`  | a, b → a / b  |

---

### 5.3 Stack Instructions

| Opcode    | Description            |
| --------- | ---------------------- |
| `POP_TOP` | Remove top of stack    |
| `DUP_TOP` | Duplicate top of stack |

---

### 5.4 Control Flow Instructions

| Opcode          | Description                   |
| --------------- | ----------------------------- |
| `JUMP`          | Set IP to target              |
| `JUMP_IF_TRUE`  | Jump if top of stack is true  |
| `JUMP_IF_FALSE` | Jump if top of stack is false |

---

### 5.5 Function Instructions

| Opcode       | Description                    |
| ------------ | ------------------------------ |
| `CALL_FUNC`  | Call function with N arguments |
| `RETURN_VAL` | Return value from function     |

---

### 5.6 Program Termination

| Opcode | Description       |
| ------ | ----------------- |
| `HALT` | Stop VM execution |

---

## 6. Execution Semantics

### Arithmetic Example

```
LOAD_CONST 2
LOAD_CONST 3
ADD
```

Stack evolution:

```
[] → [2] → [2, 3] → [5]
```

---

### Conditional Jump Example

```
LOAD_VAR x
JUMP_IF_FALSE 10
```

Execution steps:

1. Pop `x` from stack
2. If `x` is false, set IP = 10
3. Otherwise continue sequentially

---

## 7. Error Conditions

The VM raises runtime errors for:

- Invalid opcode
- Stack underflow
- Invalid jump target
- Division by zero
- Undefined variable access (if disallowed)

---

## 8. Extensibility

The bytecode format is intentionally extensible:

- New opcodes can be added without breaking existing code
- Instruction handlers are isolated from parsing logic
- Future support for:

  - Classes
  - Exceptions
  - Iterators

---

## 9. Comparison with CPython

| Feature         | CPython     | This VM              |
| --------------- | ----------- | -------------------- |
| Execution Model | Stack-based | Stack-based          |
| Bytecode        | Binary      | Textual / Structured |
| Scope           | Complex     | Explicit frames      |
| GC              | Yes         | Out of scope         |

---

## 10. Summary

This bytecode specification defines a minimal, stack-based instruction set that enables:

- Clear execution semantics
- Easy parsing and debugging
- Educational insight into Python internals
