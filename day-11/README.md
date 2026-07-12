# Day 11: Top K Dispatched Packages (Priority-Based Sorting)

## 📋 Problem Statement

A disaster management warehouse dispatches emergency supply packages one at a time, always sending the package with the **highest priority score** first. Given `N` packages with their priority scores, determine the priorities of the first `K` dispatched packages, in the exact order they leave the warehouse.

**Input Format:**
- First line: two integers `N` and `K`
- Second line: `N` space-separated integers — package priorities

**Output Format:** `K` integers — the dispatch order, in non-increasing priority

**Constraints:**
- `1 ≤ K ≤ N ≤ 10^5`
- `−2^31 ≤ Priority ≤ 2^31 − 1`

**Example:** `[12, 45, 18, 90, 27]` with `K = 2` → the two highest priorities are `90` and `45`, dispatched in that order.

---

## 🔍 Identifying the Problem

Since the dispatch always picks the current highest-priority package, the entire dispatch sequence is simply the array **sorted in descending order**. The first `K` elements of that sorted sequence are exactly the answer — no complex simulation or repeated "find max" operations are needed.

---

## 🧠 Steps of Execution

### Step 1 — Read the input
Parse `N`, `K`, and the array of priority scores from standard input.

### Step 2 — Sort in descending order
Since the highest-priority package always goes first, sorting the entire array from largest to smallest directly gives the full dispatch order.

### Step 3 — Take the first K
Slice the sorted array down to its first `K` elements — these are the packages dispatched first, already in the correct order.

### Step 4 — Print the result
Output the `K` values space-separated.

---

## 💻 Final Code

```python
def top_k_dispatch(priorities, k):
    """
    Parameters:
        priorities (list): List of package priority scores
        k (int): Number of packages to dispatch first
    Returns:
        list: Priorities of the first K dispatched packages, in order
    """
    priorities.sort(reverse=True)
    return priorities[:k]


def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0

    n = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1
    priorities = list(map(int, data[idx:idx + n])); idx += n

    result = top_k_dispatch(priorities, k)
    print(' '.join(map(str, result)))


if __name__ == "__main__":
    main()
```

---

## 🔬 Dry Run — Testcase 1

`priorities = [40, 15, 60, 25, 80, 35]`, `K = 3`

Sorted descending: `[80, 60, 40, 35, 25, 15]`

Top 3: **80 60 40** ✅

---

## ⏱ Complexity

| Metric | Complexity | Why |
|---|---|---|
| Time | O(N log N) | Dominated by the sort |
| Space | O(1) extra | Beyond the sorted output itself (in-place sorting) |

---

## 💡 What I Learned

Output formatting deserves the same care as algorithm correctness — a join with the wrong separator (or none at all) can silently mangle results, especially with negative numbers where digits can visually run together into something that looks like an entirely different value. It's worth explicitly checking the separator character used in any `join()` call before submitting, since this class of mistake produces output that's easy to overlook at a glance but still counts as a wrong answer to the judge.
