import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    size = n + 1
    
    mat = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if idx < len(data):
                mat[i][j] = int(data[idx]); idx += 1

    FULL = (1 << n) - 1
    INF = float('inf')
    dp = [[INF] * (n + 1) for _ in range(1 << n)]
    
    for i in range(1, n + 1):
        dp[1 << (i - 1)][i] = mat[0][i]

    for mask in range(1 << n):
        for i in range(1, n + 1):
            if dp[mask][i] == INF or not (mask & (1 << (i - 1))):
                continue
            for j in range(1, n + 1):
                if mask & (1 << (j - 1)):
                    continue
                nmask = mask | (1 << (j - 1))
                cost = dp[mask][i] + mat[i][j]
                if cost < dp[nmask][j]:
                    dp[nmask][j] = cost

    ans = INF
    for i in range(1, n + 1):
        total = dp[FULL][i] + mat[i][0]
        if total < ans:
            ans = total
    print(ans)

if __name__ == "__main__":
    main()
