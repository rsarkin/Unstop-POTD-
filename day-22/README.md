# Day 22: Emergency Alert Propagation (Binary Search Tree + Level Order Traversal)

## 📋 Problem Statement

An emergency alert system starts from a central command station and spreads through relay towers, where each tower can forward the message to at most two other towers. The government wants a report showing which towers received the alert at each stage — stage 0 is the central station, stage 1 is its direct neighbors, and so on. The communication hierarchy is a Binary Search Tree built by inserting the given tower IDs in order. Print the tower IDs stage by stage.

**Input Format:**
- First line: `N` (number of relay towers)
- Next `N` integers: tower IDs, inserted into the BST in the order given

**Output Format:** Tower IDs level by level, each stage on its own line

**Constraints:**
- `1 ≤ N ≤ 1000`
- `1 ≤ Tower ID ≤ 10^5`

**Example:** Inserting `10 5 15 2 7 20` builds a BST where `10` is the root, `5`/`15` are its children, and `2`/`7` are children of `5`, `20` is the right child of `15`. Stage-wise output: `10` / `5 15` / `2 7 20`.

---

## 🔍 Identifying the Problem

Strip away the emergency-broadcast framing and this is a **Binary Search Tree construction + Level Order (BFS) Traversal** problem. The description "station first, then its direct connections, then their connections..." is exactly a **BFS traversal grouped by level** — a very different traversal order from postorder (Day 19), which instead visits children before parents.

---

## 🧠 Steps of Execution

### Step 1 — Read the input
Read `N` and the `N` tower IDs.

### Step 2 — Build the BST
Insert each ID one at a time following standard BST rules — smaller goes left, larger/equal goes right.

### Step 3 — BFS level by level
Starting from the root, process nodes using a queue. At each iteration, capture the current queue size as the level boundary, pop exactly that many nodes, collect their values, and push their children for the next level.

### Step 4 — Print the report
Print each level's collected values space-separated, one line per stage.

---

## 💻 Final Code

```python
import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None: return Node(val)
    if val < root.val: root.left = insert(root.left, val)
    else: root.right = insert(root.right, val)
    return root

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    root = None
    for i in range(n):
        val = int(data[idx]); idx += 1
        root = insert(root, val)

    if root is None:
        return

    q = [root]
    front = 0
    out_lines = []
    while front < len(q):
        level_end = len(q)
        level_vals = []
        while front < level_end:
            node = q[front]; front += 1
            level_vals.append(str(node.val))
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        out_lines.append(' '.join(level_vals))

    print('\n'.join(out_lines))

if __name__ == "__main__":
    main()
```

---

## 🔬 Dry Run — Testcase 1

Input: `6 10 5 15 2 7 20`

Tree built:
```
        10
       /  \
      5    15
     / \      \
    2   7      20
```

BFS: `q=[10]` → pop 10, push 5,15 → level `"10"`
`q=[5,15]` → pop 5 (push 2,7), pop 15 (push 20) → level `"5 15"`
`q=[2,7,20]` → pop 2, pop 7, pop 20, no children → level `"2 7 20"`

**Output:**
```
10
5 15
2 7 20
```
✅

---

## ⏱ Complexity

| Metric | Complexity | Why |
|---|---|---|
| Time | O(N²) worst case, O(N log N) average | BST insertion degrades on skewed trees; BFS traversal itself is O(N) |
| Space | O(N) | Queue holds up to O(N) nodes at the widest level, plus O(N) for the tree itself |

---

## 💡 Lesson Learned

Distinguishing traversal orders from their word-problem descriptions is the real skill being tested here: "explore fully before recording" (Day 19) means postorder, while "stage by stage outward from the center" means level-order BFS. Also, a plain list with a `front` index paired with a `level_end` snapshot is a clean, import-free way to do level-order BFS without needing `collections.deque` — useful for hand-typing constraints.
