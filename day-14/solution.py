def mirror_grid(grid):
    """
    Parameters:
        grid (list of lists): The original R x C grid
    Returns:
        list of lists: Grid with each row reversed
    """
    return [row[::-1] for row in grid]


def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0

    r = int(data[idx]); idx += 1
    c = int(data[idx]); idx += 1

    grid = []
    for _ in range(r):
        row = list(map(int, data[idx:idx + c]))
        idx += c
        grid.append(row)

    result = mirror_grid(grid)

    for row in result:
        print(' '.join(map(str, row)))


if __name__ == "__main__":
    main()
