# Day 17: Minimum Announcers (Strongly Connected Components + Source Counting)

## 📋 Problem Statement

In the Kingdom of Valoria, cities are connected by one-way messenger portals. A **communication circle** is a group of cities where a messenger can travel from any city in the group to every other city in the group (a Strongly Connected Component). Once a city receives the royal announcement, every city reachable from it via portals eventually learns it too.

Princess Meera wants to place the **minimum number of initial announcers** such that every city in the kingdom eventually hears the announcement.

**Input Format:**
- First line: `N` (cities) and `M` (portals)
- Next `M` lines: `U V` — a one-way portal from city `U` to city `V`

**Output Format:** A single integer — the minimum number of initial announcers required

**Constraints:**
- `1 ≤ N ≤ 2 × 10^5`
- `0 ≤ M ≤ 3 × 10^5`
- `1 ≤ U, V ≤ N`

**Example:** With circles `{1,2,3}`, `{4}`, and `{5}`, only `{1,2,3}` and `{4}` have no incoming connection from another circle — `{5}` is reachable from `{4}` — so 2 announcers suffice.

---

## 🔍 Identifying the Problem

Strip away the kingdom framing and this is a classic **graph reachability** problem. Since portals are one-way, and groups of cities can mutually reach each other, the natural structure to find is **Strongly Connected Components (SCCs)**.

Once every SCC is collapsed into a single "super-node," the result is always a **DAG** (Directed Acyclic Graph) — a fundamental property of SCCs. In this DAG, any super-node with **at least one incoming edge** is automatically reachable once its predecessor gets the message. Only super-nodes with **zero incoming edges** (source components) genuinely need their own announcer, since nothing else in the kingdom can ever deliver the message to them. So the answer reduces to: **count the SCCs with in-degree 0 in the condensation graph.**

---

## 🧠 Steps of Execution

### Step 1 — Find all SCCs using Kosaraju's Algorithm
A two-pass approach:
- **Pass 1:** DFS on the original graph, recording each node's *finish order* (the order in which DFS calls complete).
- **Pass 2:** DFS on the **reversed** graph, processing nodes in reverse finish order — each DFS tree formed this way is exactly one SCC.

### Step 2 — Assign every city a component ID
As Pass 2 runs, label every visited city with the ID of the SCC it belongs to.

### Step 3 — Build in-degree counts for the condensation graph
For every original edge `u → v`, if `u` and `v` belong to **different** components, that's an incoming edge to `v`'s component in the condensation graph — increment its in-degree.

### Step 4 — Count source components
Any component with in-degree 0 needs its own announcer. Count them — that's the final answer.

---

## 💻 Final Code

```python
import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1

    adj = [[] for _ in range(n + 1)]
    radj = [[] for _ in range(n + 1)]
    edges = []

    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        adj[u].append(v)
        radj[v].append(u)
        edges.append((u, v))

    visited = [False] * (n + 1)
    order = []

    # Pass 1: iterative DFS on original graph, record finish order
    for start in range(1, n + 1):
        if visited[start]:
            continue
        stack = [(start, iter(adj[start]))]
        visited[start] = True
        while stack:
            node, it = stack[-1]
            advanced = False
            for nxt in it:
                if not visited[nxt]:
                    visited[nxt] = True
                    stack.append((nxt, iter(adj[nxt])))
                    advanced = True
                    break
            if not advanced:
                order.append(node)
                stack.pop()

    # Pass 2: iterative DFS on reversed graph, in reverse finish order
    comp = [0] * (n + 1)
    comp_count = 0
    visited2 = [False] * (n + 1)

    for node in reversed(order):
        if visited2[node]:
            continue
        comp_count += 1
        stack = [node]
        visited2[node] = True
        comp[node] = comp_count
        while stack:
            cur = stack.pop()
            for nxt in radj[cur]:
                if not visited2[nxt]:
                    visited2[nxt] = True
                    comp[nxt] = comp_count
                    stack.append(nxt)

    # Compute in-degree of each component in the condensation graph
    in_degree = [0] * (comp_count + 1)
    for u, v in edges:
        if comp[u] != comp[v]:
            in_degree[comp[v]] += 1

    result = sum(1 for c in range(1, comp_count + 1) if in_degree[c] == 0)
    print(result)


if __name__ == "__main__":
    main()
```

---

## 🔬 Dry Run — Testcase 1

Edges: `1→2, 2→3, 3→1, 4→5, 4→5`

SCCs found: `{1,2,3}` (mutual cycle), `{4}`, `{5}`

Checking edges between components: `4→5` connects component `{4}` to component `{5}` — so `{5}` has in-degree 1 (not a source). No edges point into `{1,2,3}` or `{4}` from anywhere else — both have in-degree 0.

**Source components: `{1,2,3}` and `{4}` → answer = 2** ✅

---

## ⏱ Complexity

| Metric | Complexity | Why |
|---|---|---|
| Time | O(N + M) | Kosaraju's algorithm performs two linear passes over the graph |
| Space | O(N + M) | Adjacency lists (forward + reversed), plus per-node auxiliary arrays |

---

## 💡 Lesson Learned

This problem is a clean real-world illustration of **condensation graphs** — once any directed graph's SCCs are collapsed, the result is always a DAG, and DAG properties (like "a node with in-degree 0 has no possible predecessor") become directly usable for reasoning about reachability. It's also a good reminder that with `N` up to `200000`, **iterative DFS with an explicit stack** is the safer default over recursion — a straightforward recursive DFS would risk hitting Python's recursion depth limit on a long chain-shaped graph, which the given constraints don't rule out.
