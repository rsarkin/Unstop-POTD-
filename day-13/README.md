# Day 13: Longest Reconstruction Chain (Longest Increasing Subsequence)

## 📋 Problem Statement

During a solar storm in 2487, fragments of an interplanetary transmission were corrupted. Each recovered fragment has a reliability score. Fragments can only be connected in a chain if each score is **strictly greater** than the previous — any decrease or equality breaks the chain. Determine the length of the **longest valid reconstruction chain**.

**Input Format:**
- First line: `N`
- Second line: `N` space-separated integers — fragment reliability scores

**Output Format:** A single integer — the length of the longest strictly increasing chain

**Constraints:**
- `1 ≤ N ≤ 200000`
- `1 ≤ score[i] ≤ 10^9`

**Example:** `[1, 7, 3, 5, 9, 4, 8, 10]` → the chain `1 → 3 → 5 → 8 → 10` has length 5.

---

## 🔍 Identifying the Problem

Strip away the sci-fi framing and this is the classic **Longest Increasing Subsequence (LIS)** problem — find the longest subsequence (not necessarily contiguous) where each element is strictly greater than the one before it.

With `N` up to `200000`, the well-known O(N²) DP solution becomes too slow — around `4 × 10^10` operations in the worst case. This calls for the optimized **O(N log N)** technique.

---

## 🧠 Steps of Execution

### Step 1 — Maintain a "smallest tail" array
Keep a list `tails`, where `tails[k]` holds the smallest possible ending value of any increasing chain of length `k+1` found so far. This list stays sorted, which unlocks binary search.

### Step 2 — Process each score in order
Binary search `tails` to find where each score belongs:
- If larger than everything in `tails` → extends the longest chain so far → append it.
- Otherwise → replaces the first tail value that is `≥` it, since a smaller tail leaves more room for future extensions.

### Step 3 — Use `bisect_left` to enforce strict increase
Ensures equal values get replaced rather than treated as an extension.

### Step 4 — Read off the answer
The final length of `tails` is the length of the longest valid chain.

---

## 💻 Optimized Solution — O(N log N)

```python
from bisect import bisect_left

def longest_chain(scores):
    """
    Parameters:
        scores (list): List of fragment reliability scores
    Returns:
        int: Length of the longest strictly increasing chain
    """
    tails = []

    for score in scores:
        pos = bisect_left(tails, score)
        if pos == len(tails):
            tails.append(score)
        else:
            tails[pos] = score

    return len(tails)


def main():
    import sys
    data = sys.stdin.read().split()
    idx = 0

    n = int(data[idx]); idx += 1
    scores = list(map(int, data[idx:idx + n])); idx += n

    result = longest_chain(scores)
    print(result)


if __name__ == "__main__":
    main()
```

---

## 💻 Simpler Solution — O(N²) DP

For building intuition before optimizing: for every fragment, look at every earlier fragment with a smaller score and take the longest chain ending there, plus 1.

```python
def longest_chain_simple(scores):
    """
    Parameters:
        scores (list): List of fragment reliability scores
    Returns:
        int: Length of the longest strictly increasing chain
    """
    n = len(scores)
    dp = [1] * n   # every fragment is at least a chain of length 1 by itself

    for i in range(n):
        for j in range(i):
            if scores[j] < scores[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    scores = list(map(int, data[1:n + 1]))
    print(longest_chain_simple(scores))


if __name__ == "__main__":
    main()
```

**Trade-off:** easier to reason about, but too slow for the full constraint range (`N` up to 200000) — useful for understanding the recurrence, not for the actual submission.

---

## 🔬 Dry Run — Testcase 0

`scores = [1, 7, 3, 5, 9, 4, 8, 10]`

| score | tails before | action | tails after |
|---|---|---|---|
| 1 | [] | append | [1] |
| 7 | [1] | append | [1,7] |
| 3 | [1,7] | replace | [1,3] |
| 5 | [1,3] | append | [1,3,5] |
| 9 | [1,3,5] | append | [1,3,5,9] |
| 4 | [1,3,5,9] | replace | [1,3,4,9] |
| 8 | [1,3,4,9] | replace | [1,3,4,8] |
| 10 | [1,3,4,8] | append | [1,3,4,8,10] |

**Final length: 5** ✅

---

## ⏱ Complexity

| Version | Time | Space |
|---|---|---|
| Optimized (binary search) | O(N log N) | O(N) |
| Simpler (DP) | O(N²) | O(N) |

Optimized version verified at N = 200,000 with random data — completed in ~0.13 seconds.

---

## 💡 Lesson Learned

There are often two valid solutions to the same problem at different complexity tiers — a simpler O(N²) DP that's easy to reason about, and a sharper O(N log N) approach using binary search over a carefully maintained "smallest tail" array. Starting with the intuitive version first to confirm correctness on the samples, then upgrading to the optimized version for the actual large-N submission, is a solid general strategy: get it *right* before making it *fast*.
