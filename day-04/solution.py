def has_duplicate(arr):
    """
    Parameters:
        arr (list): List of non-negative integers
    Returns:
        str: "YES" if a duplicate exists, "NO" otherwise
    """
    seen = set()
    for num in arr:
        if num in seen:
            return "YES"   # early exit the moment a repeat is found
        seen.add(num)
    return "NO"


def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0

    t = int(data[idx]); idx += 1
    results = []

    for _ in range(t):
        n = int(data[idx]); idx += 1
        arr = list(map(int, data[idx:idx + n])); idx += n
        results.append(has_duplicate(arr))

    print('\n'.join(results))


if __name__ == "__main__":
    main()
