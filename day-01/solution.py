def smallest_max_difference(arr, k):
    from collections import deque

    n = len(arr)
    if k <= 0 or k > n:
        return -1

    max_dq = deque()
    min_dq = deque()
    result = float('inf')

    for i in range(n):
        while max_dq and arr[max_dq[-1]] <= arr[i]:
            max_dq.pop()
        max_dq.append(i)

        while min_dq and arr[min_dq[-1]] >= arr[i]:
            min_dq.pop()
        min_dq.append(i)

        window_start = i - k + 1
        if max_dq[0] < window_start:
            max_dq.popleft()
        if min_dq[0] < window_start:
            min_dq.popleft()

        if i >= k - 1:
            current_diff = arr[max_dq[0]] - arr[min_dq[0]]
            if current_diff < result:
                result = current_diff

    return result


def main():
    import sys
    data = sys.stdin.read().split()

    idx = 0
    n = int(data[idx]); idx += 1
    arr = list(map(int, data[idx:idx+n])); idx += n
    k = int(data[idx]); idx += 1

    result = smallest_max_difference(arr, k)
    print(result)


if __name__ == "__main__":
    main()