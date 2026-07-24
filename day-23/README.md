# Day 23: Sacred Crystal Guardian Pairing (Bitmask DP — Maximum Weight Perfect Matching)

## 📋 Problem Statement

Exactly `2N` guardians must be paired into `N` ceremonial pairs to protect the Sacred Crystal. Every pair of guardians has a known compatibility score, and the total ceremony strength is the sum of compatibility scores across all chosen pairs. Every guardian must belong to exactly one pair. Determine the maximum total compatibility achievable across all valid pairings.

**Input Format:**
- First line: `N` (number of pairs to form)
- Next `2N` lines: a `2N × 2N` symmetric compatibility matrix, with diagonal entries `0`

**Output Format:** A single integer — the maximum total compatibility score

**Constraints:**
- `1 ≤ N ≤ 10`
- `0 ≤ Compatibility Score ≤ 10^6`
- Matrix is symmetric, diagonal is `0`

**Example:** With 4 guardians and matrix `[[0,8,5,6],[8,0,7,4],[5,7,0,9],[6,4,9,0]]`, pairing `(G1,G2)+(G3,G4)` gives `8+9=17`, the maximum among all 3 possible pairings.

---

## 🔍 Identifying the Problem

Strip away the ceremonial framing and this is **Maximum Weight Perfect Matching** on a complete graph — pair up all `2N` nodes to maximize total edge weight. With `2N ≤ 20`, brute-forcing all `(2N-1)!!` pairings is infeasible for larger N (654,729,075 ways when N=10), but a bitmask over 20 bits (`2^20 ≈ 1M` states) is completely tractable — this is the classic signal for **Bitmask DP**.

The key trick that keeps the state space clean: at every state, only pair the **smallest-indexed unpaired guardian**, never all possible pairs blindly. This guarantees every valid full pairing is generated exactly once, since the smallest unpaired guardian is always resolved first — avoiding duplicate counting of the same pairing in different orders.

---

## 🧠 Steps of Execution

### Step 1 — Read the input
Read `N` and build the `2N × 2N` compatibility matrix.

### Step 2 — Define the recursive state
`solve(mask)` = maximum total compatibility achievable by fully pairing up all guardians *not yet* set in `mask`. Base case: if `mask` covers everyone, return `0`.

### Step 3 — Always resolve the smallest unpaired guardian first
Find the lowest-indexed bit not set in `mask` — call it `first`. Try pairing `first` with every other unpaired guardian `j`, recursing into `solve(mask | bit_first | bit_j)`.

### Step 4 — Memoize
Cache each `solve(mask)` result in a flat memoization list initialized with `-1` so overlapping subproblems (the same set of paired guardians reached via different pairing orders) aren't recomputed. Using a flat list is much faster in Python than a dictionary lookup.

### Step 5 — Return the answer
`solve(0)` — starting with nobody paired — gives the maximum total compatibility.

---

## 💻 Final Code

```python
import sys
sys.setrecursionlimit(3000)

def solve(mask, total, comp, memo):
    if mask == (1 << total) - 1:
        return 0
    if memo[mask] != -1:
        return memo[mask]
    
    # Find the first unpaired guardian (index of the lowest unset bit in mask)
    # Using bitwise: ~mask & (mask + 1) isolates the lowest unset bit as a power of 2.
    first = (~mask & (mask + 1)).bit_length() - 1
    
    best = 0
    for j in range(first + 1, total):
        if not (mask & (1 << j)):
            score = comp[first][j] + solve(mask | (1 << first) | (1 << j), total, comp, memo)
            if score > best:
                best = score
    
    memo[mask] = best
    return best

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    total = 2 * n
    comp = []
    idx = 1
    for i in range(total):
        row = []
        for j in range(total):
            row.append(int(input_data[idx]))
            idx += 1
        comp.append(row)
    
    memo = [-1] * (1 << total)
    print(solve(0, total, comp, memo))

if __name__ == "__main__":
    main()
```

---

## 🔬 Dry Run — Testcase 1

Input: `2 / 0 8 5 6 / 8 0 7 4 / 5 7 0 9 / 6 4 9 0`

- `solve(0000)`: first unpaired = guardian 0. Try pairing with 1, 2, 3:
  - Pair (0,1): `8 + solve(0011)`
  - Pair (0,2): `5 + solve(0101)`
  - Pair (0,3): `6 + solve(1001)`
- `solve(0011)` (0,1 paired): first unpaired = 2. Pair (2,3): `9 + solve(1111) = 9 + 0 = 9`. Total: `8+9=17`
- `solve(0101)` (0,2 paired): first unpaired = 1. Pair (1,3): `4 + 0 = 4`. Total: `5+4=9`
- `solve(1001)` (0,3 paired): first unpaired = 1. Pair (1,2): `7 + 0 = 7`. Total: `6+7=13`
- `best = max(17, 9, 13) = 17`

**Output: `17`** ✅

---

## ⏱ Complexity

| Metric | Complexity | Why |
|---|---|---|
| Time | O(2^(2N) × N) | Each of the up to `2^(2N)` reachable masks is resolved once (memoized), with up to O(N) pairing choices per state |
| Space | O(2^(2N)) | Memo array stores results for all $2^{2N}$ masks, plus O(2N) recursion depth |

---

## 💡 Lesson Learned

Maximum weight perfect matching is a distinct bitmask DP pattern from TSP (Day 21) — instead of tracking "current position + visited set," it only needs "which nodes remain unpaired," and the *"always resolve the smallest unpaired element first"* trick is the key to avoiding duplicate work when order doesn't matter (a pair is a pair, regardless of which guardian in it gets picked "first"). Recursion with memoization also turned out cleaner than an iterative mask sweep here, since the recursive definition mirrors the plain-English idea directly, and the call stack automatically guarantees subproblems are solved before they're needed. Furthermore, using a pre-allocated flat array instead of a dictionary for memoization prevents excessive hash table lookups and object overhead in Python.
