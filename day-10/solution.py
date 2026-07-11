from collections import Counter

def top_visitor(ids):
    """
    Parameters:
        ids (list): List of visitor IDs (with repeats)
    Returns:
        tuple: (visitor_id, frequency) of the most frequent visitor,
               smallest ID wins ties
    """
    c = Counter(ids)
    # max picks highest count first; for ties, -id makes the smallest id win
    best = max(c.items(), key=lambda x: (x[1], -x[0]))
    return best[0], best[1]


def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    ids = list(map(int, data[1:n + 1]))
    v, cnt = top_visitor(ids)
    print(v, cnt)


if __name__ == "__main__":
    main()
