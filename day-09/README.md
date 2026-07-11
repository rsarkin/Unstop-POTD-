# Day 09: Top of the Pile (Stack Simulation)

## 📋 Problem Statement

An archive room stores records in a vertical pile — new records go on top, and archivists always remove from the top since records underneath aren't directly accessible. Given a sequence of operations, determine the value of the record visible at the top after all operations are processed.

**Operations:**
- `ADD X` → place record `X` on top of the pile
- `REMOVE` → remove the current top record

**Input Format:**
- First line: `N` — number of operations
- Next `N` lines: one operation each

**Output Format:** The value at the top after all operations, or `-1` if the pile is empty

**Constraints:**
- `1 ≤ N ≤ 100000`
- `1 ≤ X ≤ 1000000000`

---

## 🔍 Identifying the Problem

Strip away the archive-room framing and the behavior described — "always add to the top, always remove from the top" — is the textbook definition of a **stack** (Last-In-First-Out / LIFO). Python's built-in `list` already behaves exactly like a stack when restricted to `.append()` and `.pop()`, so no custom data structure is needed.

---

## 🧠 Steps of Execution

### Step 1 — Parse all operations
Read `N`, then read each operation, distinguishing `ADD X` from `REMOVE`.

### Step 2 — Simulate with a stack
Maintain a list acting as the pile:
- `ADD X` → push `X` onto the end of the list.
- `REMOVE` → pop the last element off — but only if the list isn't already empty, to avoid crashing on an invalid removal.

### Step 3 — Report the final state
After all operations: if the stack still has elements, the last one is the visible top. If the stack is empty, print `-1`.

---

## 🔬 Dry Run — Testcase 0

`ADD 10, ADD 20, ADD 30, REMOVE, ADD 40`

| Operation | Stack after |
|---|---|
| ADD 10 | [10] |
| ADD 20 | [10, 20] |
| ADD 30 | [10, 20, 30] |
| REMOVE | [10, 20] |
| ADD 40 | [10, 20, 40] |

**Top = 40** ✅

---

## ⏱ Complexity

| Metric | Complexity | Why |
|---|---|---|
| Time | O(N) | Single pass through the operations |
| Space | O(N) | Worst case, if every operation is `ADD` |

---

## ✅ No Blunders This Time

Verified cleanly against both official testcases plus an edge case: calling `REMOVE` on an already-empty pile, which is safely guarded against with a non-empty check before popping, avoiding an `IndexError`.

**Why this one's worth noting:** it's a clean example of recognizing when a real-world description ("always add/remove from the top") maps directly onto a known data structure — no need to overengineer when the built-in `list` already provides exactly the right push/pop behavior.
