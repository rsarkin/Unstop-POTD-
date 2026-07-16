def min_dream_energy(p):
    """
    Parameters:
        p (list): List of N+1 dimensions defining the frame chain
    Returns:
        int: Minimum total dream-energy required to fuse the entire chain
    """
    n = len(p) - 1  # number of frames
    dp = [[0] * n for _ in range(n)]

    # length = size of the chain segment being solved (2 frames, 3 frames, ...)
    for length in range(2, n + 1):
        for i in range(0, n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[0][n - 1]


def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0

    n = int(data[idx]); idx += 1
    p = list(map(int, data[idx:idx + n + 1])); idx += n + 1

    result = min_dream_energy(p)
    print(result)


if __name__ == "__main__":
    main()
