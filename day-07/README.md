# Day 07: Farthest City from the Capital (BFS on a Tree)

## 📋 Problem Statement

In the ancient Kingdom of Arvandor, cities are connected through a network of roads such that there is **exactly one possible route** between any two cities — this is the defining structure of a **tree**. City 1 is the capital.

The king defines the "distance" of a city as the number of roads that must be crossed to travel from the capital to it. Cities directly connected to the capital have distance 1, cities two roads away have distance 2, and so on.

**Task:** Determine the **maximum distance** from City 1 to any other city in the kingdom.

**Input Format:**
- First line: `N` — number of cities
- Next `N-1` lines: two integers `U` and `V` — a road connecting City `U` and City `V`

**Output Format:** A single integer — the maximum number of roads that must be traveled to reach the farthest city from City 1

**Constraints:**
- `1 ≤ N ≤ 200000`
- `1 ≤ U, V ≤ N`

**Example:** A tree rooted at City 1 with City 7 reachable via `1 → 3 → 6 → 7` (3 roads) is the farthest city, giving an answer of `3`.

---

## 🔍 Identifying the Problem

Strip away the kingdom framing and this is a graph traversal problem on a **tree** — exactly `N` cities and `N-1` roads with no cycles, guaranteeing a single unique path between any two cities. The question boils down to: **starting from a root node, what is the maximum depth (in edges) reachable in this tree?**

Since every road counts equally as "1 unit of distance" and the graph has no cycles, this is a textbook case for **Breadth-First Search (BFS)** — it explores the tree level by level, so the distance to each city is discovered the moment that city is first visited.

---

## 🧠 Steps of Execution

### Step 1 — Build the graph as an adjacency list
Roads are bidirectional, so for every `(U, V)` pair, add `V` to `U`'s neighbor list and `U` to `V`'s neighbor list.

### Step 2 — Run BFS from City 1
Start a queue with `(City 1, distance 0)`. Use a `visited` array to avoid revisiting cities.

### Step 3 — Expand level by level
For each city dequeued, look at all its neighbors. Any unvisited neighbor gets `distance + 1` and is enqueued — this guarantees each city's distance is discovered in the correct, shortest number of steps from the capital.

### Step 4 — Track the maximum distance seen
As each city is processed, compare its distance against a running `max_distance` and update accordingly.

### Step 5 — Return the final maximum
Once the queue is empty, every reachable city has been visited, and `max_distance` holds the answer.

---

## 🔬 Dry Run — Testcase 0

Tree structure:
```
        1
      /   \
     2     3
    / \     \
   4   5     6
              \
               7
```

BFS expansion order: `1(0) → 2(1), 3(1) → 4(2), 5(2), 6(2) → 7(3)`

**Farthest city: City 7, at distance 3** ✅

---

## ⏱ Complexity

| Metric | Complexity | Why |
|---|---|---|
| Time | O(N) | Each city and each road is visited exactly once during BFS |
| Space | O(N) | Adjacency list, visited array, and queue all scale with N |

Verified at N = 200,000 with a worst-case straight-chain tree — completed in ~1.06 seconds.

---

## 🐛 Design Decision Worth Noting (Not a Blunder, But a Deliberate Choice)

**Why BFS instead of DFS:** A recursive DFS could technically compute the same distances by tracking depth as it recurses, but with `N` up to `200000`, a straight-chain tree (like Testcase 1's structure: `1-2-3-4-5-6-7-8`, scaled up) would force Python's recursive DFS **200,000 levels deep** — well past Python's default recursion limit, causing a crash (`RecursionError`).

**Why this matters:** BFS sidesteps this entirely because it's naturally **iterative**, using an explicit queue on the heap instead of the call stack. This was chosen proactively during the design phase rather than discovered as a bug — worth documenting as a case where picking the right traversal strategy *upfront* avoids an entire class of failure that would only show up on large/adversarial test inputs, not on the small sample testcases.

**Lesson:** When working with trees or graphs where `N` can be large, always consider the worst-case shape (a long chain, not just a balanced tree) before choosing between recursive DFS and iterative BFS/stack-based DFS.
