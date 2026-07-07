# Day 05: Maximum Crystals with No Two Adjacent Chambers (House Robber Pattern)

## Problem Statement

Deep beneath the capital city lies an ancient vault system with a sequence of chambers arranged in a corridor, each containing a certain number of energy crystals. Aria can open any chamber, but the vault's security system triggers if **two adjacent chambers** are both opened.

Given `N` chambers with crystal counts, determine the **maximum total crystals** Aria can collect while ensuring no two selected chambers are adjacent.

**Example:** `[5] [8] [4] [10] [3]` → opening chambers with `8` and `10` gives `18` crystals (can't open `8` and `4` together since they're adjacent).

**Input Format:**
- First line: `N` — number of chambers
- Second line: `N` space-separated integers — crystals in each chamber

**Output Format:** A single integer — the maximum crystals collectible

**Constraints:**
- `1 ≤ N ≤ 100000`
- `1 ≤ crystals[i] ≤ 10^9`

## Approach / Thought Process

This is the classic **House Robber** dynamic programming pattern. At each chamber, we have a binary decision to make:
1. **Skip the current chamber**: The maximum crystals collectible up to this point is the same as the maximum crystals collectible up to the previous chamber (`prev1`).
2. **Open the current chamber**: The maximum crystals collectible up to this point is the crystals in the current chamber plus the maximum crystals collectible up to two chambers prior (`prev2 + crystals[i]`).

This gives us the recurrence relation:
```
dp[i] = max(dp[i-1], dp[i-2] + crystals[i])
```

### Space Optimization
Since `dp[i]` only depends on the two preceding states (`dp[i-1]` and `dp[i-2]`), we do not need to maintain a full DP array. Instead, we can use two rolling variables (`prev1` and `prev2`) to track the values. This reduces our space complexity from $O(N)$ to $O(1)$.

## Dry Run — Testcase 0

`crystals = [5, 8, 4, 10, 3]`

| Chamber | value | current = max(prev1, prev2+value) | prev2 | prev1 |
|---|---|---|---|---|
| start | – | – | 0 | 0 |
| 1 | 5 | max(0, 0+5) = 5 | 0 | 5 |
| 2 | 8 | max(5, 0+8) = 8 | 5 | 8 |
| 3 | 4 | max(8, 5+4) = 9 | 8 | 9 |
| 4 | 10 | max(9, 8+10) = 18 | 9 | 18 |
| 5 | 3 | max(18, 9+3) = 18 | 18 | 18 |

**Final answer: 18** ✅

## Complexity

- **Time:** $O(N)$ — Single pass traversal through the crystal counts list.
- **Space:** $O(1)$ — Only two rolling variables `prev1` and `prev2` are used.

## What I Learned
Unlike some other dynamic programming or partitioning problems that have subtle asymmetric edge cases, the House Robber pattern has a clean, unambiguous recurrence relation. When state transitions only depend on a fixed window of preceding states (e.g., $i-1$ and $i-2$), rolling variables offer an elegant way to optimize space to $O(1)$ while keeping the logic simple and easy to reason about.
