# Day 20: Bridge Waiting Line (Queue Simulation)

## 📋 Problem Statement

A suspension bridge only allows a limited number of vehicles at a time. Vehicles arrive and join a waiting line (`ENTER X`), and vehicles leave when they finish crossing, freeing up the front of the line (`EXIT`). Given a sequence of `N` recorded events, determine which vehicle is at the front of the waiting line at the end of the day, or report `EMPTY` if no vehicles are waiting.

**Input Format:**
- First line: `N` (number of recorded events)
- Next `N` lines: either `ENTER X` or `EXIT`

**Output Format:** The ID of the vehicle at the front of the waiting line, or `EMPTY`

**Constraints:**
- `1 ≤ N ≤ 10^5`
- `1 ≤ X ≤ 10^9`

**Example:** Events `ENTER 10, ENTER 20, ENTER 30, EXIT, ENTER 40, EXIT, ENTER 50` leave the line as `[30, 40, 50]` → front is `30`.

---

## 🔍 Identifying the Problem

Strip away the bridge framing and this is a straightforward **queue simulation** problem. Vehicles are processed in FIFO order — the first vehicle to arrive is the first to be granted permission. `ENTER X` is a push to the back of the queue, and `EXIT` is a pop from the front. The only subtlety is that an `EXIT` on an empty line must be a no-op rather than an error.

---

## 🧠 Steps of Execution

### Step 1 — Read the input
Read `N` and the `N` events.

### Step 2 — Maintain a queue with a front pointer
Instead of physically removing elements from the front of a list (which is costly), use a growing list along with a `front` index that marks how many elements have already "exited."

### Step 3 — Process each event
For `ENTER X`, append `X` to the list. For `EXIT`, advance the `front` pointer by one — but only if there's still something left to remove.

### Step 4 — Report the result
After processing all events, if `front` still points to a valid index, print that vehicle's ID; otherwise print `EMPTY`.

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
    q = []
    front = 0
    for _ in range(n):
        if idx >= len(data):
            break
        event = data[idx]; idx += 1
        if event == "ENTER":
            if idx < len(data):
                x = data[idx]; idx += 1
                q.append(x)
        elif event == "EXIT":
            if front < len(q):
                front += 1
    print(q[front] if front < len(q) else "EMPTY")

if __name__ == "__main__":
    main()
```

---

## 🔬 Dry Run — Testcase 1

Input: `7 ENTER 10 ENTER 20 ENTER 30 EXIT ENTER 40 EXIT ENTER 50`

- `ENTER 10` → `q=[10]`, `front=0`
- `ENTER 20` → `q=[10,20]`, `front=0`
- `ENTER 30` → `q=[10,20,30]`, `front=0`
- `EXIT` → `front=1` (10 is now "gone")
- `ENTER 40` → `q=[10,20,30,40]`, `front=1`
- `EXIT` → `front=2` (20 is now "gone")
- `ENTER 50` → `q=[10,20,30,40,50]`, `front=2`

`q[front] = q[2] = 30`

**Output: `30`** ✅

---

## ⏱ Complexity

| Metric | Complexity | Why |
|---|---|---|
| Time | O(N) | Each event is processed in O(1) — a single append or pointer increment |
| Space | O(N) | The list stores up to N vehicle IDs (front pointer avoids costly removals) |

---

## 💡 Lesson Learned

FIFO "line" or "queue" problems described through everyday scenarios (bridges, ticket counters, printers) are simulation problems where the trick is picking the right underlying structure. A `deque` is the natural fit for true O(1) pops from both ends, but when hand-typing code, a plain list with a `front` index achieves the same amortized efficiency without needing an extra import — a useful lightweight substitute for `collections.deque` in constrained environments.
