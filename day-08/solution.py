def find_unique_id(ids):
    """
    Parameters:
        ids (list): List of registration IDs, where every ID appears
                     exactly twice except one which appears once
    Returns:
        int: The registration ID that appears exactly once
    """
    result = 0
    for reg_id in ids:
        result ^= reg_id
    return result


def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    ids = list(map(int, data[1:n + 1]))
    print(find_unique_id(ids))


if __name__ == "__main__":
    main()
