# Day 18: Synchronized Drums (GCD / LCM)

## 📋 Problem Statement

During the Grand River Festival, two ceremonial drums are struck together at time 0. Kabir's drum beats every `A` seconds, and Tara's drum beats every `B` seconds. Determine the next time after the start when both drums beat simultaneously again.

**Input Format:** Two integers `A` and `B`

**Output Format:** A single integer — the time of the next simultaneous beat

**Constraints:**
- `1 ≤ A, B ≤ 10^5`

**Example:** Kabir beats every 4 sec (`4, 8, 12, ...`), Tara beats every 6 sec (`6, 12, 18, ...`). They next align at `12`.

---

## 🔍 Identifying the Problem

Strip away the festival framing and this is a **math / number theory** problem, not a data structure or search problem. Kabir's beats occur at every multiple of `A`, Tara's at every multiple of `B`. The next time both patterns coincide is the smallest number that is a multiple of both — the classic definition of the **LCM (Least Common Multiple)**.

---

## 🧠 Steps of Execution

### Step 1 — Compute GCD(A, B)
Use the Euclidean algorithm (`math.gcd`) to find the greatest common divisor of the two intervals.

### Step 2 — Compute LCM using the GCD identity
Apply the identity `LCM(A, B) = (A × B) // GCD(A, B)` — this avoids overflow-prone brute-force loops that check every multiple one by one.

### Step 3 — Print the result
That LCM value is the earliest time both drums beat together again.

---

## 💻 Final Code

```python
import sys
import math

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    
    A = int(data[idx]); idx += 1
    B = int(data[idx]); idx += 1
    
    # LCM = (A * B) / GCD(A, B)
    g = math.gcd(A, B)
    lcm = (A * B) // g
    
    print(lcm)

if __name__ == "__main__":
    main()
```

---

## 🔬 Dry Run — Testcase 1

Input: `4 6`
- `gcd(4, 6) = 2`
- `lcm = (4 × 6) // 2 = 24 // 2 = 12`

**Output: `12`** ✅

Input: `5 8`
- `gcd(5, 8) = 1`
- `lcm = (5 × 8) // 1 = 40`

**Output: `40`** ✅

---

## ⏱ Complexity

| Metric | Complexity | Why |
|---|---|---|
| Time | O(log(min(A, B))) | Euclidean algorithm for GCD converges logarithmically |
| Space | O(1) | Only a few integer variables are used |

---

## 💡 Lesson Learned

Story problems about repeating or periodic events syncing up ("every X seconds", "every Y minutes", "meet again", "beat together") are almost always **LCM problems in disguise**. Computing LCM via `(A * B) // gcd(A, B)` rather than looping through multiples is a pattern worth recognizing instantly — it's O(log n) instead of O(n), and it sidesteps any risk of missing the correct alignment point on large inputs.
