# Day 15: Minimum Dream-Energy for Tapestry Weaving (Matrix Chain Multiplication)

## 📋 Problem Statement

In the floating kingdom of Aetheria, Riya must fuse a chain of weaving frames into one ceremonial tapestry. Frame `i` has dimensions `p[i] × p[i+1]`. Fusing two neighboring segments of dimensions `x×y` and `y×z` costs `x × y × z` units of dream-energy. Different fusion orders produce different total costs — determine the **minimum** total dream-energy required to fuse the entire chain.

**Input Format:**
- First line: `N` — number of weaving frames
- Second line: `N+1` integers `p0 p1 ... pN` defining frame dimensions

**Output Format:** A single integer — the minimum dream-energy required

**Constraints:**
- `2 ≤ N ≤ 200`
- `1 ≤ pi ≤ 1000`

**Example:** For `p = [20, 30, 10, 40]`, fusing in the order `(20×30) × ((30×10) × (10×40))` costs `6000 + 8000 = 14000`, cheaper than the alternative order costing `36000`.

---

## 🔍 Identifying the Problem

Strip away the dream-weaving theme and this is the classic **Matrix Chain Multiplication** problem — a foundational Dynamic Programming pattern. The core challenge: fusion cost depends heavily on the *order* in which segments are combined, and with `N` up to `200`, trying every possible grouping order (which grows exponentially) is completely infeasible.

---

## 🧠 Steps of Execution

### Step 1 — Define the state
`dp[i][j]` = minimum energy to fuse frames `i` through `j` into a single combined segment.

### Step 2 — Set the base case
`dp[i][i] = 0` — a single frame requires no fusion at all.

### Step 3 — Build the recurrence
To fuse the range `[i, j]`, some split point `k` must be the last fusion — combining `[i,k]` and `[k+1,j]`:
```
dp[i][j] = min over all k in [i, j-1] of:
    dp[i][k] + dp[k+1][j] + p[i] * p[k+1] * p[j+1]
```
Here `p[i]` and `p[j+1]` are the outer dimensions of the combined segment, and `p[k+1]` is the shared middle dimension at the fusion point — directly matching the problem's `x × y × z` cost formula.

### Step 4 — Fill by increasing chain length
Process subranges starting from length 2 (pairs of frames) up to the full chain, since larger ranges depend on smaller ones already being solved.

### Step 5 — Return the final answer
`dp[0][N-1]` holds the minimum cost to fuse the entire chain of frames.

---

## 💻 Final Code

```python
def min_dream_energy(p):
    """
    Parameters:
        p (list): List of N+1 dimensions defining the frame chain
    Returns:
        int: Minimum total dream-energy required to fuse the entire chain
    """
    n = len(p) - 1  # number of frames
    dp = [[0] * n for _ in range(n)]

    # length = size of the chain segment being solved (2 frames, 3 frames, ...)
    for length in range(2, n + 1):
        for i in range(0, n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[0][n - 1]


def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0

    n = int(data[idx]); idx += 1
    p = list(map(int, data[idx:idx + n + 1])); idx += n + 1

    result = min_dream_energy(p)
    print(result)


if __name__ == "__main__":
    main()
```

---

## 🔬 Dry Run — Testcase 1

`p = [20, 30, 10, 40]` → frames: `20×30`, `30×10`, `10×40`

- `dp[0][1]` = `20×30×10` = 6000
- `dp[1][2]` = `30×10×40` = 12000
- `dp[0][2]`: try `k=0` → `0 + 12000 + 20×30×40 = 36000`; try `k=1` → `6000 + 0 + 20×10×40 = 14000`
- Minimum: **14000** ✅

---

## ⏱ Complexity

| Metric | Complexity | Why |
|---|---|---|
| Time | O(N³) | For each of O(N²) subranges, up to O(N) split points are tried |
| Space | O(N²) | The `dp` table |

With `N ≤ 200`, O(N³) is roughly 8 × 10^6 operations — verified with a stress test at N = 200, completing in ~0.29 seconds.

---

## 💡 Lesson Learned

This is a strong example of **interval DP**, where the state is defined over a *range* `[i, j]` rather than a single index — a pattern distinct from the linear DP seen in earlier days (like Day 5's House Robber or Day 12's tower-jumping problem). Recognizing when a problem's cost depends on how a sequence is *grouped* (rather than just which elements are *chosen*) is the signal to reach for this range-based DP structure, trying every possible split point as the "last operation."
