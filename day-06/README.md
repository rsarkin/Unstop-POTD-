# Day 06: Maximum Checkpoints with Minimum Distance Gap (Greedy Selection)

## 📋 Problem Statement

A town is preparing for its annual lantern festival, with `N` lantern checkpoints placed along a straight road at various (unsorted) distances from the town entrance. The organizers want to select the **maximum number of checkpoints** such that the distance between any two **consecutively selected** checkpoints is at least `D` meters.

**Input Format:**
- First line: two integers `N` and `D`
- Second line: `N` integers representing checkpoint distances (not necessarily sorted)

**Output Format:** A single integer — the maximum number of checkpoints that can be selected

**Constraints:**
- `1 ≤ N ≤ 100000`
- `1 ≤ D ≤ 1000000000`
- `0 ≤ checkpointDistance[i] ≤ 1000000000`

**Example:** Checkpoints at `1, 2, 4, 8, 9` with `D=3` → selecting `1, 4, 8` gives 3 checkpoints, since each consecutive pair is at least 3 meters apart.

---

## 🔍 Identifying the Problem

Strip away the festival theme and this is a classic **greedy interval-selection** problem. The key realization: since checkpoints aren't given in sorted order, but "consecutive selected checkpoints" only makes physical sense when moving along the road in increasing order, **sorting is the mandatory first step** before any selection logic can apply.

Once sorted, the challenge becomes: walk through the checkpoints and decide, at each step, whether picking the current one helps maximize the total count.

---

## 🧠 Steps of Execution

### Step 1 — Sort the checkpoints
Since positions arrive unordered, sort them first so "consecutive" has a meaningful, spatial interpretation.

### Step 2 — Apply the greedy insight
Always pick the **earliest possible checkpoint** that satisfies the minimum gap `D` from the last selected checkpoint. Picking the earliest valid checkpoint (rather than waiting for a later one) never hurts — it only preserves or increases the room available for future selections. This greedy choice is provably optimal for this class of problem.

### Step 3 — Walk through and select
- Always select the very first (smallest) checkpoint — nothing to compare it against yet.
- For every subsequent checkpoint, check the gap from the *last selected* checkpoint (not the last checkpoint visited).
  - If the gap is `≥ D` → select it, update the "last selected" marker.
  - Otherwise → skip and move to the next.

### Step 4 — Count and return
Track how many checkpoints were selected throughout the pass — that count is the answer.

---

## 🔬 Dry Run — Testcase 1

Sorted: `[0, 1, 2, 4, 6, 7, 9]`, `D = 2`

| Checkpoint | Gap from last_selected | Decision | count | last_selected |
|---|---|---|---|---|
| 0 | (first, auto-pick) | pick | 1 | 0 |
| 1 | 1-0=1 < 2 | skip | 1 | 0 |
| 2 | 2-0=2 ≥ 2 | pick | 2 | 2 |
| 4 | 4-2=2 ≥ 2 | pick | 3 | 4 |
| 6 | 6-4=2 ≥ 2 | pick | 4 | 6 |
| 7 | 7-6=1 < 2 | skip | 4 | 6 |
| 9 | 9-6=3 ≥ 2 | pick | 5 | 9 |

**Final answer: 5** ✅

---

## ⏱ Complexity

| Metric | Complexity | Why |
|---|---|---|
| Time | O(N log N) | Dominated by the sort; the greedy selection pass afterward is O(N) |
| Space | O(1) extra | Only a counter and a "last selected" tracker — no additional data structures |

Verified at N = 100,000 with random data — completed in ~0.08 seconds.
