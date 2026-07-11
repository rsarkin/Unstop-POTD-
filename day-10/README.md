# Day 10: Most Frequent Visitor ID (with Tie-Breaking)

## 📋 Problem Statement

During the Kingdom of Vardania's cultural festival, visitor IDs are recorded every time a visitor enters an event zone. Given the full sequence of recorded IDs, find:
1. The Visitor ID that appears the **maximum number of times**
2. Its **frequency**

If multiple Visitor IDs share the highest frequency, output the **smallest** Visitor ID among them.

**Input Format:**
- First line: `N` — number of entries in the ledger
- Second line: `N` space-separated integers — the Visitor IDs

**Output Format:** Two integers separated by a space — the most frequent Visitor ID and its count

**Constraints:**
- `1 ≤ N ≤ 10^5`
- `−2^31 ≤ Visitor ID ≤ 2^31 − 1`

**Example:** `[101, 205, 101, 310, 205, 101, 205]` → both `101` and `205` appear 3 times each, but `101` is smaller, so the answer is `101 3`.

---

## 🔍 Identifying the Problem

This is a **frequency-counting problem with a tie-breaking rule** — closely related to Day 04's duplicate detection, but a step further: instead of just detecting whether a value repeats, we need the *exact count* of every value, plus a deterministic way to pick a winner when multiple values are tied for the top spot.

---

## 🧠 Steps of Execution

### Step 1 — Count occurrences of every ID
Build a frequency table mapping each Visitor ID to how many times it appears in the ledger.

### Step 2 — Select the best candidate
Scan through the frequency table to find the entry with the highest count. When ties occur, prefer the smaller ID.

### Step 3 — Print the result
Output the winning ID and its frequency.

---

## 💻 Final Code

```python
from collections import Counter

def top_visitor(ids):
    """
    Parameters:
        ids (list): List of visitor IDs (with repeats)
    Returns:
        tuple: (visitor_id, frequency) of the most frequent visitor,
               smallest ID wins ties
    """
    c = Counter(ids)
    # max picks highest count first; for ties, -id makes the smallest id win
    best = max(c.items(), key=lambda x: (x[1], -x[0]))
    return best[0], best[1]


def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    ids = list(map(int, data[1:n + 1]))
    v, cnt = top_visitor(ids)
    print(v, cnt)


if __name__ == "__main__":
    main()
```

---

## 🔬 Dry Run — Testcase 1

`ids = [4, 8, 4, 2, 8, 8, 1, 4]`

Frequency table: `{4: 3, 8: 3, 2: 1, 1: 1}`

Both `4` and `8` tie at frequency `3`. The tie-break key `(count, -id)` favors the smaller ID → `4` wins.

**Result: 4 3** ✅

---

## ⏱ Complexity

| Metric | Complexity | Why |
|---|---|---|
| Time | O(N) | One pass to build the `Counter`, one pass over unique IDs to find the best |
| Space | O(N) | Frequency table in the worst case (all unique IDs) |

---

## 💡 What I Learned

Once a brute-force-but-correct solution is verified, it's often worth a second pass to reach for the right built-in tool (`Counter`, `max` with a custom key) — not for performance here since both versions are O(N), but for **readability and conciseness**, which matters when documenting solutions for a public repo.
