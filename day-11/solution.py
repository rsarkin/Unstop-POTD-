def top_k_dispatch(priorities, k):
    """
    Parameters:
        priorities (list): List of package priority scores
        k (int): Number of packages to dispatch first
    Returns:
        list: Priorities of the first K dispatched packages, in order
    """
    priorities.sort(reverse=True)
    return priorities[:k]


def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0

    n = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1
    priorities = list(map(int, data[idx:idx + n])); idx += n

    result = top_k_dispatch(priorities, k)
    print(' '.join(map(str, result)))


if __name__ == "__main__":
    main()
