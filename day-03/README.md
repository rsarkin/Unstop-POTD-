# Day 3: Cycle Detection & Chain Recovery in a Corrupted Linked List

## 📋 Problem Statement

In a corrupted data forwarding system, each node is linked to at most one other node via a pointer. Due to system failures, some forwarding chains may contain cycles or become disconnected.

Given a collection of `N` nodes — each with a unique `node_id`, an integer `value`, and a `next_id` pointer (or `-1` for null) — the task is to:

1. Starting from a given `start_id`, traverse the forwarding chain using only pointer manipulation.
2. Recover the longest possible simple (cycle-free) chain starting from that node.
3. Break any cycle in-place by setting the `.next` of the first repeating node to `null`.
4. Print the values of the nodes in the recovered chain, from start to end, space-separated.

**Hard constraint:** No arrays, hash maps, or sets allowed for cycle detection — only pointer manipulation with **O(1) extra memory**.

**Constraints:**
- `1 ≤ N ≤ 10⁵`
- All `node_id`s are distinct positive integers
- `value ∈ [-10⁶, 10⁶]`
- `next_id` is either `-1` or a valid `node_id`

---

## 🔍 Identifying the Real Problem

Strip away the "corrupted data" story and this is a classic computer science problem in disguise: **linked list cycle detection and removal.**

The tricky part isn't detecting *whether* a cycle exists — that's well known. The real constraint is **how**: since hash sets/arrays for tracking visited nodes are explicitly banned, the only way to satisfy O(1) extra memory is a two-pointer technique.

This immediately points to **Floyd's Cycle Detection Algorithm** (Tortoise and Hare) — the standard technique for exactly this constraint.

---

## 🧠 Steps of Execution

### Step 1 — Build the linked structure
Since input arrives as a flat list of `(node_id, value, next_id)` tuples, first construct actual `Node` objects and link them via `.next` pointers using their `next_id`. (This dictionary is only for *construction* — it plays no role in the cycle detection logic itself.)

### Step 2 — Detect a cycle (Tortoise and Hare)
Move a `slow` pointer one step at a time and a `fast` pointer two steps at a time, starting both at `head`.
- If `fast` reaches `None`, there's no cycle.
- If `slow` and `fast` ever land on the same node, a cycle exists.

### Step 3 — Locate the exact start of the cycle
Once `slow` and `fast` meet, reset a fresh pointer to `head`. Move it and `slow` **one step at a time simultaneously**. The node where they meet is mathematically guaranteed to be the cycle's starting node — a well-known property of Floyd's algorithm.

### Step 4 — Break the cycle
Walk around the cycle starting from that node until finding the node whose `.next` points *back* to the cycle start. That node is the "last node before the repeat" — set its `.next = None` to sever the loop.

### Step 5 — Traverse and collect
Walk the now-clean chain from `head` to `None`, collecting each node's `value`.

### Step 6 — Print
Join the collected values with spaces and print.

---

## 💻 Final Code

```python
class Node:
    def __init__(self, node_id, value, next_id):
        self.node_id = node_id
        self.value = value
        self.next_id = next_id
        self.next = None


def recover_chain(n, node_details, start_id):
    # Step 1: Build all Node objects (dict used only for construction,
    # NOT for cycle detection -- that stays pointer-only, O(1) extra space)
    nodes = {}
    for node_id, value, next_id in node_details:
        nodes[node_id] = Node(node_id, value, next_id)

    for node_id, value, next_id in node_details:
        if next_id != -1:
            nodes[node_id].next = nodes[next_id]

    head = nodes[start_id]

    # Step 2: Floyd's Tortoise and Hare -- detect a cycle
    slow = head
    fast = head
    has_cycle = False

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            has_cycle = True
            break

    # Step 3 & 4: locate the cycle start, then break the link
    if has_cycle:
        slow2 = head
        while slow2 is not slow:
            slow2 = slow2.next
            slow = slow.next
        cycle_start = slow

        temp = cycle_start
        while temp.next is not cycle_start:
            temp = temp.next

        temp.next = None  # cut the repeating link

    # Step 5: traverse the now cycle-free chain
    result = []
    current = head
    while current is not None:
        result.append(current.value)
        current = current.next

    return result


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    n = int(data[0])
    node_details = []
    for i in range(1, n + 1):
        node_id, value, next_id = map(int, data[i].split())
        node_details.append((node_id, value, next_id))
    start_id = int(data[n + 1])
    result = recover_chain(n, node_details, start_id)
    print(' '.join(map(str, result)))  # Step 6: print space-separated

if __name__ == "__main__":
    main()
```

---

## ⏱ Complexity

| Metric | Complexity | Why |
|---|---|---|
| Time | O(N) | Cycle detection, cycle-start search, cycle walk, and final traversal are each linear passes |
| Space | O(1) extra | Only pointer variables (`slow`, `fast`, `temp`) used for detection — the dict is purely for building the graph from raw input, not part of the algorithm's memory footprint |

---

## 🐛 Blunder & Fix

**What happened:** Final output printed as `1234` instead of `1 2 3 4`.

**Root cause:** Used `''.join(map(str, result))` (empty-string separator) instead of `' '.join(map(str, result))` (space separator). The entire algorithm — cycle detection, breaking, traversal — was already 100% correct; this was purely a formatting slip in the print statement.

```python
# Before:
print(''.join(map(str, result)))

# After:
print(' '.join(map(str, result)))
```

**Lesson:** Algorithm correctness and output formatting are two separate things to verify. A solution can compute exactly the right values and still fail a judge if the output format (spacing, casing, delimiters) doesn't match exactly — always double-check formatting requirements independently, even after the core logic is proven correct.
