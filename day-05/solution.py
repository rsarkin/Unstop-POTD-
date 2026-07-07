def max_crystals(crystals):
    """
    Parameters:
        crystals (list): List of integers representing crystals in each chamber
    Returns:
        int: Maximum crystals collectible with no two adjacent chambers opened
    """
    prev2 = 0  # best total using chambers up to i-2
    prev1 = 0  # best total using chambers up to i-1

    for value in crystals:
        current = max(prev1, prev2 + value)
        prev2 = prev1
        prev1 = current

    return prev1


def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0

    n = int(data[idx]); idx += 1
    crystals = list(map(int, data[idx:idx + n])); idx += n

    result = max_crystals(crystals)
    print(result)


if __name__ == "__main__":
    main()
