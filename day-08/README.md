# Day 08: Find the Unique Registration ID (XOR Trick)

## 📋 Problem Statement

Every year, Willowbrook hosts a grand celebration where guests register twice (online and offline forms) — except one guest who registered only once. Given a list of `N` registration IDs where every ID appears exactly twice except one, find the ID that appears exactly once.

**Input Format:**
- First line: `N` — number of registration records
- Second line: `N` space-separated integers — the registration IDs

**Output Format:** A single integer — the registration ID that appears exactly once

**Constraints:**
- `1 ≤ N ≤ 10^5`
- `0 ≤ Registration ID ≤ 10^9`
- Exactly one ID appears once; every other ID appears exactly twice

---

## 🔍 Identifying the Problem

Strip away the celebration story and this is the classic **"Single Number"** problem. A hash-map frequency count would work, but it costs extra memory. There's a much sharper tool available here: the **XOR operator**.

---

## 🧠 Steps of Execution

XOR (exclusive OR, represented by the `^` symbol) has special properties that make it perfect for this task:
1. **Self-Inverse**: `x ^ x = 0`. Any number XOR-ed with itself cancels out to zero.
2. **Identity**: `x ^ 0 = x`. XOR-ing any number with zero leaves the number unchanged.
3. **Commutative & Associative**: The order of operations does not matter (e.g., `a ^ b ^ a = (a ^ a) ^ b = 0 ^ b = b`).

So, if every ID appears exactly twice except for one, XOR-ing the entire list together cancels out all paired IDs, leaving only the unpaired one standing.

---

## 🔬 Dry Run — Testcase 1

Input:
`ids = [101, 202, 303, 101, 202, 404, 303]`

We compute the running XOR of the elements:
- Start: `result = 0`
- Grouping: `(101 ^ 101) ^ (202 ^ 202) ^ (303 ^ 303) ^ 404`
- Calculation: `0 ^ 0 ^ 0 ^ 404 = 404`

Every ID except `404` appears twice, so all of them cancel out via XOR.

**Result: 404** ✅

---

## ⏱ Complexity

| Metric | Complexity | Why |
|---|---|---|
| Time | O(N) | Single pass through the input array of size N |
| Space | O(1) | Just one running variable — no hash map or extra array needed |

---

## ✅ No Blunders This Time

Verified cleanly against official sample cases plus edge cases:
- A single-element list (e.g., `N = 1` and `ids = [0]`) where the result is immediately output.
- The unique ID being `0`.
- The unique ID appearing at the very start of the list.
- A stress test at `N = 100,000` (completed in ~0.06 seconds).

The XOR trick is a small piece of bit-manipulation insight that turns what looks like a counting problem into something solvable in a single line inside the loop — a good pattern to keep in the back pocket for similar "find the odd one out" problems.
