def max_checkpoints(checkpoints, d):
    """
    Parameters:
        checkpoints (list): List of checkpoint distances (unsorted)
        d (int): Minimum required gap between consecutive selected checkpoints
    Returns:
        int: Maximum number of checkpoints that can be selected
    """
    checkpoints.sort()

    count = 1                       # always pick the first (smallest) checkpoint
    last_selected = checkpoints[0]

    for i in range(1, len(checkpoints)):
        if checkpoints[i] - last_selected >= d:
            count += 1
            last_selected = checkpoints[i]

    return count


def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0

    n = int(data[idx])
    idx += 1
    d = int(data[idx])
    idx += 1
    checkpoints = list(map(int, data[idx:idx + n]))
    idx += n

    result = max_checkpoints(checkpoints, d)
    print(result)


if __name__ == "__main__":
    main()
