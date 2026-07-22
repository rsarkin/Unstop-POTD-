# Day 21: Relay Network Restoration (Travelling Salesman Problem — Bitmask DP)

## 📋 Problem Statement

Commander Aarav must travel from the Central Dock (location 0) to activate all `N` dormant relays exactly once each, then return to the Central Dock. Travel between any two locations has a known energy cost (not necessarily symmetric). Determine the minimum total energy required to activate every relay and return to the dock.

**Input Format:**
- First line: `N` (number of relays)
- Next `N+1` lines: an `(N+1) × (N+1)` energy matrix, where row `i`/column `j` is the energy to travel directly from location `i` to `j`. Location `0` is the Central Dock, locations `1..N` are relays.

**Output Format:** A single integer — the minimum total energy for the round trip

**Constraints:**
- `1 ≤ N ≤ 16`
- `0 ≤ Energy ≤ 10^6`
- `Energy(i, i) = 0`
- The matrix is not necessarily symmetric

**Example:** With N=2 and matrix `[[0,4,9],[6,0,3],[5,8,0]]`, route `0→1→2→0` costs `4+3+5=12`, cheaper than `0→2→1→0` = 23. Answer: `12`.

---

## 🔍 Identifying the Problem

Strip away the space-colony framing and this is the classic **Travelling Salesman Problem (TSP)** — visit every node exactly once and return to the start, minimizing total cost. The constraint `N ≤ 16` is the strongest signal here: it rules out brute-force permutations (`16!` is far too large) and rules out greedy approaches (they don't guarantee optimality), and instead points directly to **Bitmask Dynamic Programming (the Held-Karp algorithm)**, which handles up to ~20 nodes comfortably.

---

## 🧠 Steps of Execution

### Step 1 — Read the energy matrix
Read `N` and build the `(N+1) × (N+1)` matrix, where index `0` is the dock and `1..N` are relays.

### Step 2 — Define the DP state
`dp[mask][i]` = minimum energy to have activated exactly the relays in `mask`, currently standing at relay `i`. Represent `mask` as a bitmask where bit `i-1` set means relay `i` is activated.

### Step 3 — Base case
Starting from the dock directly to each relay `i`: `dp[1<<(i-1)][i] = mat[0][i]`.

### Step 4 — Transition
For every reachable state `(mask, i)`, try extending to any unvisited relay `j`: update `dp[mask | (1<<(j-1))][j]` with `dp[mask][i] + mat[i][j]` if it's smaller.

### Step 5 — Close the loop
Once `mask` equals the full set of relays, the answer is `min over i of dp[full][i] + mat[i][0]` — the cost to return to the dock from whichever relay was activated last.

---

## 💻 Final Code

```python
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    size = n + 1
    
    mat = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if idx < len(data):
                mat[i][j] = int(data[idx]); idx += 1

    FULL = (1 << n) - 1
    INF = float('inf')
    dp = [[INF] * (n + 1) for _ in range(1 << n)]
    
    for i in range(1, n + 1):
        dp[1 << (i - 1)][i] = mat[0][i]

    for mask in range(1 << n):
        for i in range(1, n + 1):
            if dp[mask][i] == INF or not (mask & (1 << (i - 1))):
                continue
            for j in range(1, n + 1):
                if mask & (1 << (j - 1)):
                    continue
                nmask = mask | (1 << (j - 1))
                cost = dp[mask][i] + mat[i][j]
                if cost < dp[nmask][j]:
                    dp[nmask][j] = cost

    ans = INF
    for i in range(1, n + 1):
        total = dp[FULL][i] + mat[i][0]
        if total < ans:
            ans = total
    print(ans)

if __name__ == "__main__":
    main()
```

---

## 🔬 Dry Run — Testcase 1

Input: `2  0 4 9  6 0 3  5 8 0`

- `mat = [[0,4,9],[6,0,3],[5,8,0]]`, `n=2`, `FULL = 0b11`
- Base case: `dp[0b01][1] = mat[0][1] = 4`, `dp[0b10][2] = mat[0][2] = 9`
- From `dp[0b01][1]=4`, extend to relay 2: `dp[0b11][2] = 4 + mat[1][2] = 4+3 = 7`
- From `dp[0b10][2]=9`, extend to relay 1: `dp[0b11][1] = 9 + mat[2][1] = 9+8 = 17`
- Close loop: `dp[0b11][1] + mat[1][0] = 17+6 = 23`; `dp[0b11][2] + mat[2][0] = 7+5 = 12`
- `ans = min(23, 12) = 12`

**Output: `12`** ✅

---

## ⏱ Complexity

| Metric | Complexity | Why |
|---|---|---|
| Time | O(N² × 2^N) | For each of `2^N` masks, iterate over `N` current positions and `N` next positions |
| Space | O(N × 2^N) | DP table has one entry per (mask, node) pair |

---

## 💡 Lesson Learned

`N ≤ 16` (or generally up to ~20) in a "visit everything exactly once, minimize cost" problem is a strong, near-guaranteed signal for **bitmask DP / Held-Karp**, since it's the sweet spot where `2^N` is tractable but `N!` is not. Also, while hand-typing flattened code, indentation mismatches (mixing tab-equivalent spacing, or a line silently losing a level of indent) are the most common source of errors — when Python throws an `IndentationError` or a variable "not defined" that should clearly be in scope, the fastest fix is deleting and retyping the whole line fresh rather than trying to patch individual leading spaces.
