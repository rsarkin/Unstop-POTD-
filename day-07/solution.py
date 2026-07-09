from collections import deque

def max_distance_from_capital(n, edges):
    """
    Parameters:
        n (int): Number of cities
        edges (list): List of (u, v) tuples representing roads
    Returns:
        int: Maximum distance (in roads) from City 1 to any other city
    """
    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # BFS from City 1
    visited = [False] * (n + 1)
    visited[1] = True
    queue = deque()
    queue.append((1, 0))

    max_distance = 0

    while queue:
        city, dist = queue.popleft()
        max_distance = max(max_distance, dist)

        for neighbor in adj[city]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, dist + 1))

    return max_distance


def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0

    n = int(data[idx])
    idx += 1

    edges = []
    for _ in range(n - 1):
        if idx >= len(data):
            break
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        edges.append((u, v))

    result = max_distance_from_capital(n, edges)
    print(result)


if __name__ == "__main__":
    main()
