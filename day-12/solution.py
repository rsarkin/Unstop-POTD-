def min_energy(energy):
    """
    Parameters:
        energy (list): List of energy values at each tower
    Returns:
        int: Minimum energy required to travel from the first to the last tower
    """
    n = len(energy)
    dp = [float('inf')] * n
    dp[0] = 0

    for j in range(1, n):
        for i in range(j):
            cost = abs(energy[i] - energy[j]) * (j - i)
            if dp[i] + cost < dp[j]:
                dp[j] = dp[i] + cost

    return dp[n - 1]


def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0

    n = int(data[idx]); idx += 1
    energy = list(map(int, data[idx:idx + n])); idx += n

    result = min_energy(energy)
    print(result)


if __name__ == "__main__":
    main()
