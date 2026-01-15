# 📝 Python VM Stack Diagram Guide

### **Legend**

- `[...]` → current stack (bottom → top)
- `TOS` → Top Of Stack
- `pop()` → remove top element
- `push(x)` → push element onto stack

---

## **1⃣ Stack Manipulation**

| Instruction        | Stack Before | Operation           | Stack After       | Notes                    |
| ------------------ | ------------ | ------------------- | ----------------- | ------------------------ |
| `LOAD_CONST <val>` | `[...]`      | push constant       | `[..., val]`      | Push literal onto stack  |
| `LOAD_VAR <name>`  | `[...]`      | push variable value | `[..., value]`    | Read from locals/globals |
| `STORE_VAR <name>` | `[..., val]` | pop TOS → store     | `[...]`           | Write to locals/globals  |
| `POP_TOP`          | `[..., val]` | pop TOS             | `[...]`           | Remove top of stack      |
| `DUP_TOP`          | `[..., val]` | push(copy of TOS)   | `[..., val, val]` | Duplicate top value      |

---

## **2⃣ Arithmetic Operations**

| Instruction | Stack Before  | Operation                   | Stack After  | Notes                 |
| ----------- | ------------- | --------------------------- | ------------ | --------------------- |
| `ADD`       | `[..., a, b]` | pop b, pop a → push(a + b)  | `[..., a+b]` | Binary addition       |
| `SUB`       | `[..., a, b]` | pop b, pop a → push(a - b)  | `[..., a-b]` | Binary subtraction    |
| `MUL`       | `[..., a, b]` | pop b, pop a → push(a \* b) | `[..., a*b]` | Binary multiplication |
| `DIV`       | `[..., a, b]` | pop b, pop a → push(a / b)  | `[..., a/b]` | Binary division       |
| `NEG`       | `[..., a]`    | pop a → push(-a)            | `[..., -a]`  | Unary negation        |

> ⚠ Important: pop order is always **last-in, first-out**. The first popped value is **right operand**.

---

## **3⃣ Control Flow**

| Instruction              | Stack Before  | Operation                      | Stack After | Notes                     |
| ------------------------ | ------------- | ------------------------------ | ----------- | ------------------------- |
| `JUMP <target>`          | `[...]`       | set IP = target                | `[...]`     | Unconditional jump        |
| `JUMP_IF_TRUE <target>`  | `[..., cond]` | pop cond → if True: IP=target  | `[...]`     | Conditional jump if True  |
| `JUMP_IF_FALSE <target>` | `[..., cond]` | pop cond → if False: IP=target | `[...]`     | Conditional jump if False |
| `HALT`                   | `[...]`       | stop execution                 | `[...]`     | Stop VM                   |

---

## **4⃣ Function Call / Return**

| Instruction     | Stack Before                         | Operation                                                 | Stack After             | Notes                                              |
| --------------- | ------------------------------------ | --------------------------------------------------------- | ----------------------- | -------------------------------------------------- |
| `CALL_FUNC <N>` | `[..., func, arg1, arg2, ..., argN]` | pop N args → pop func → call(func(\*args)) → push(result) | `[..., result]`         | Function call (args pushed first, TOS is last arg) |
| `RETURN_VAL`    | `[..., val]`                         | pop val → return to caller                                | caller stack: push(val) | Return value to calling frame                      |

> ⚠ Important: argument order is **bottom to top** of stack. Example:

```
Stack before CALL_FUNC 2: [func, 10, 20]
Popped: 20 (b), 10 (a), func
Called: func(10, 20)
Result pushed: result
Stack after: [result]
```

---

## **5⃣ Example: Simple Arithmetic Bytecode**

```text
# Compute (2 + 3) * 4
LOAD_CONST 2      # Stack: [2]
LOAD_CONST 3      # Stack: [2,3]
ADD               # Stack: [5]
LOAD_CONST 4      # Stack: [5,4]
MUL               # Stack: [20]
STORE_VAR result  # Stack: []
HALT              # Stop
```

---

## **6⃣ Example: Function Call Bytecode**

```text
# Compute add(10, 20)
LOAD_VAR add      # Stack: [add function]
LOAD_CONST 10     # Stack: [add, 10]
LOAD_CONST 20     # Stack: [add, 10, 20]
CALL_FUNC 2       # Pops: 20, 10, add → pushes 30
STORE_VAR result  # Stack: []
HALT
```

---

## ✅ Summary / Tips

1. **Always track TOS** for binary operations: first pop → right operand, second pop → left operand.
2. **Push function first, then args** before `CALL_FUNC`.
3. `RETURN_VAL` expects **one value on stack** to return.
4. `JUMP_IF_TRUE/FALSE` pops the condition.
5. `DUP_TOP` and `POP_TOP` only affect the stack, no IP change.
