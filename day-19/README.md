# Day 19: Chamber Recovery Sequence (Binary Search Tree + Postorder Traversal)

## 📋 Problem Statement

Deep beneath an abandoned kingdom, chambers are arranged in a branching structure where each chamber connects to at most two deeper chambers. Historians enter a chamber, fully explore the left side, then fully explore the right side, and only then record the artifact in the current chamber. Given `N` artifact numbers inserted in order to build this structure (a Binary Search Tree), determine the final recovery sequence historians would record.

**Input Format:**
- First line: `N` (number of artifacts)
- Next `N` integers: artifact numbers, inserted into the BST in the order given

**Output Format:** The recovery sequence, space-separated

**Constraints:**
- `1 ≤ N ≤ 1000`
- `1 ≤ Artifact Number ≤ 10^5`

**Example:** Inserting `25 15 35 10 20` builds a BST where `25` is root, `15`/`35` are its children, and `10`/`20` are children of `15`. The recovery sequence is `10 20 15 35 25`.

---

## 🔍 Identifying the Problem

Strip away the chamber framing and this is a classic **Binary Search Tree construction + tree traversal** problem. The phrase "explore left fully, then right fully, then record current" is a direct description of **postorder traversal** (Left → Right → Root). The real task is simply: build a BST by inserting the given numbers, then print its postorder traversal.

---

## 🧠 Steps of Execution

### Step 1 — Read the input
Read `N` and the `N` artifact numbers.

### Step 2 — Build the BST
Insert each number one at a time following standard BST rules — smaller values go into the left subtree, larger/equal values go into the right subtree.

### Step 3 — Traverse the tree in postorder
Recursively visit the left subtree, then the right subtree, and finally record the current node's value.

### Step 4 — Print the sequence
Join the collected values and print them space-separated.

---

## 💻 Final Code

```python
import sys
sys.setrecursionlimit(2000)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def postorder(root, result):
    if root is None:
        return
    postorder(root.left, result)
    postorder(root.right, result)
    result.append(str(root.val))

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    
    n = int(data[idx]); idx += 1
    root = None
    for _ in range(n):
        val = int(data[idx]); idx += 1
        root = insert(root, val)
    
    result = []
    postorder(root, result)
    print(' '.join(result))

if __name__ == "__main__":
    main()
```

---

## 🔬 Dry Run — Testcase 1

Input: `5 25 15 35 10 20`

Insertions build:
```
        25
       /  \
     15    35
    /  \
  10    20
```

Postorder: visit `10` (no children) → record `10`; visit `20` (no children) → record `20`; back at `15`, both sides done → record `15`; visit `35` (no children) → record `35`; back at `25`, both sides done → record `25`.

**Output: `10 20 15 35 25`** ✅

---

## ⏱ Complexity

| Metric | Complexity | Why |
|---|---|---|
| Time | O(N²) worst case, O(N log N) average | BST insertion degrades to O(N) per insert on a skewed tree; postorder itself is O(N) |
| Space | O(N) | O(N) for tree nodes, plus recursion stack up to O(N) on a skewed tree |

---

## 💡 Lesson Learned

A word-problem describing "explore left fully, then right fully, then note the current spot" is just postorder traversal in disguise — recognizing traversal order patterns hidden in story form is often the real puzzle, not the coding itself. Recursive tree code (`insert`/`postorder`) is far more compact and readable than simulating a tree with parallel arrays, as long as `N` stays small enough that recursion depth isn't a concern.
