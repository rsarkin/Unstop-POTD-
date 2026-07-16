from bisect import bisect_left

def longest_chain(scores):
    """
    Optimized O(N log N) solution using binary search (bisect_left) over the tails array.

    Parameters:
        scores (list): List of fragment reliability scores
    Returns:
        int: Length of the longest strictly increasing chain
    """
    tails = []

    for score in scores:
        pos = bisect_left(tails, score)
        if pos == len(tails):
            tails.append(score)
        else:
            tails[pos] = score

    return len(tails)


def longest_chain_simple(scores):
    """
    Simpler O(N^2) DP solution for intuition and reference.

    Parameters:
        scores (list): List of fragment reliability scores
    Returns:
        int: Length of the longest strictly increasing chain
    """
    n = len(scores)
    if n == 0:
        return 0
    dp = [1] * n   # every fragment is at least a chain of length 1 by itself

    for i in range(n):
        for j in range(i):
            if scores[j] < scores[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0

    n = int(data[idx]); idx += 1
    scores = list(map(int, data[idx:idx + n])); idx += n

    # By default, use the optimized version to support N up to 200,000
    result = longest_chain(scores)
    print(result)


if __name__ == "__main__":
    main()
