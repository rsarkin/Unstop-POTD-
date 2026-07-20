import sys


def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
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
