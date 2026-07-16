# Day 14: Mirror Mode — Reverse Each Row of a Grid

## 📋 Problem Statement

A technology company tests digital billboards using a "Mirror Mode" that reflects the display content horizontally. Given a rectangular grid of brightness values, row positions stay unchanged, but within each row, the values must be reversed — the leftmost value becomes the rightmost, and so on.

**Input Format:**
- First line: two integers `R` and `C`
- Next `R` lines: `C` integers each

**Output Format:** The reflected grid — each row reversed, row order unchanged

**Constraints:**
- `1 ≤ R, C ≤ 100`
- `0 ≤ value ≤ 1000`

**Example:** Row `[1, 2, 3]` becomes `[3, 2, 1]`; each row is reversed independently, other rows are unaffected.

---

## 🔍 Identifying the Problem

Strip away the billboard framing and this is a direct **row-wise array reversal** task — no complex algorithm needed, just applying a reversal operation to each row of a 2D grid while keeping the row order intact.

---

## 🧠 Steps of Execution

### Step 1 — Read the grid dimensions and contents
Parse `R` and `C`, then read `R` rows of `C` integers each into a 2D list.

### Step 2 — Reverse each row independently
For every row in the grid, reverse the order of its elements. The row's position in the grid stays exactly where it was — only the contents within that row flip.

### Step 3 — Print the result
Output each reversed row, space-separated, preserving the original row order.

---

## 💻 Final Code

```python
def mirror_grid(grid):
    """
    Parameters:
        grid (list of lists): The original R x C grid
    Returns:
        list of lists: Grid with each row reversed
    """
    return [row[::-1] for row in grid]


def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0

    r = int(data[idx]); idx += 1
    c = int(data[idx]); idx += 1

    grid = []
    for _ in range(r):
        row = list(map(int, data[idx:idx + c]))
        idx += c
        grid.append(row)

    result = mirror_grid(grid)

    for row in result:
        print(' '.join(map(str, row)))


if __name__ == "__main__":
    main()
```

---

## 🔬 Dry Run — Testcase 1

Grid:
```
1 2 3
4 5 6
```

Row 1 `[1, 2, 3]` reversed → `[3, 2, 1]`
Row 2 `[4, 5, 6]` reversed → `[6, 5, 4]`

**Output:**
```
3 2 1
6 5 4
```
✅ Matches expected output.

---

## ⏱ Complexity

| Metric | Complexity | Why |
|---|---|---|
| Time | O(R × C) | Every cell in the grid is visited exactly once |
| Space | O(R × C) | For storing the resulting reversed grid |

---

## ✅ No Blunders This Time

Verified cleanly against both official testcases plus edge cases: a single row, a single column (where reversal has no visible effect since each row has only one element), and a trivial 1×1 grid.
