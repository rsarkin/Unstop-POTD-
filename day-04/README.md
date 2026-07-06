# Day 04: Duplicate Detection in an Array

## 📋 Problem Statement

You are given an array containing `N` non-negative integers. Your task is to determine whether any value occurs more than once in the array.

If at least one duplicate element is present, print `YES`. Otherwise, print `NO`.

**Input Format:**
- First line: `T` — number of test cases
- For each test case: first line is `N` (array size), second line is `N` space-separated integers

**Output Format:**
For each test case, print `YES` if the array contains one or more duplicate values, `NO` if all elements are distinct.

**Constraints:**
- `1 ≤ T ≤ 50`
- `1 ≤ N ≤ 10^5`
- `0 ≤ arr[i] ≤ 10^5`

---

## 🔍 Identifying the Problem

Strip away the framing and this is the classic **duplicate detection** problem, repeated across multiple test cases. The only real design decision is *how* to detect the duplicate efficiently, since `N` can be as large as `10^5` and this runs up to `50` times.

**Brute force** (compare every pair) is O(N²) per test case — with N = 10^5, that's up to 10^10 operations per test case, which would time out immediately.

The natural efficient structure here is a **hash set**: it lets us check "have I seen this value before?" in O(1) average time, turning the whole problem into a single linear pass.

---

## 🧠 Steps of Execution

### Step 1 — Read all test cases
Parse `T`, then for each test case read `N` and the array of `N` integers.

### Step 2 — Walk through the array once, tracking seen values
Maintain a `seen` set. For each number:
- If it's already in `seen` → a duplicate has been found → return `YES` immediately (no need to keep scanning).
- Otherwise, add it to `seen` and continue.

### Step 3 — Handle the "no duplicate" case
If the loop finishes without ever finding a repeat, every element was unique → return `NO`.

### Step 4 — Repeat for every test case, print all results
Collect the answer for each test case and print them one per line.

---

## 💻 Final Code

```python
def has_duplicate(arr):
    """
    Parameters:
        arr (list): List of non-negative integers
    Returns:
        str: "YES" if a duplicate exists, "NO" otherwise
    """
    seen = set()
    for num in arr:
        if num in seen:
            return "YES"   # early exit the moment a repeat is found
        seen.add(num)
    return "NO"


def main():
    import sys
    data = sys.stdin.read().split()
    idx = 0

    t = int(data[idx]); idx += 1
    results = []

    for _ in range(t):
        n = int(data[idx]); idx += 1
        arr = list(map(int, data[idx:idx + n])); idx += n
        results.append(has_duplicate(arr))

    print('\n'.join(results))


if __name__ == "__main__":
    main()
```

---

## ⏱ Complexity

| Metric | Complexity | Why |
|---|---|---|
| Time | O(N) per test case | Single pass through the array; set lookups and insertions are O(1) average |
| Space | O(N) per test case | For the `seen` set holding up to N unique values |
