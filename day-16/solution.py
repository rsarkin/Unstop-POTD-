import sys


def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    q = int(data[idx]); idx += 1
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        a[i] = int(data[idx]); idx += 1

    size = 4 * (n + 1)
    sum_ = [0] * size
    mx1 = [0] * size
    mx2 = [-1] * size
    cnt = [0] * size

    sys.setrecursionlimit(300000)

    def pushup(node):
        left = 2 * node
        right = 2 * node + 1
        sum_[node] = sum_[left] + sum_[right]
        if mx1[left] == mx1[right]:
            mx1[node] = mx1[left]
            cnt[node] = cnt[left] + cnt[right]
            mx2[node] = max(mx2[left], mx2[right])
        elif mx1[left] > mx1[right]:
            mx1[node] = mx1[left]
            cnt[node] = cnt[left]
            mx2[node] = max(mx2[left], mx1[right])
        else:
            mx1[node] = mx1[right]
            cnt[node] = cnt[right]
            mx2[node] = max(mx1[left], mx2[right])

    def build(node, l, r):
        if l == r:
            sum_[node] = a[l]
            mx1[node] = a[l]
            mx2[node] = -1
            cnt[node] = 1
            return
        mid = (l + r) // 2
        build(2 * node, l, mid)
        build(2 * node + 1, mid + 1, r)
        pushup(node)

    def push_tag(node, v):
        if v >= mx1[node]:
            return
        sum_[node] -= (mx1[node] - v) * cnt[node]
        mx1[node] = v

    def pushdown(node):
        lm = mx1[node]
        left = 2 * node
        right = 2 * node + 1
        if mx1[left] > lm:
            push_tag(left, lm)
        if mx1[right] > lm:
            push_tag(right, lm)

    def update(node, l, r, ql, qr, v):
        if qr < l or r < ql or mx1[node] <= v:
            return
        if ql <= l and r <= qr and mx2[node] < v:
            push_tag(node, v)
            return
        mid = (l + r) // 2
        pushdown(node)
        update(2 * node, l, mid, ql, qr, v)
        update(2 * node + 1, mid + 1, r, ql, qr, v)
        pushup(node)

    def query(node, l, r, ql, qr):
        if qr < l or r < ql:
            return 0
        if ql <= l and r <= qr:
            return sum_[node]
        mid = (l + r) // 2
        pushdown(node)
        return query(2 * node, l, mid, ql, qr) + query(2 * node + 1, mid + 1, r, ql, qr)

    build(1, 1, n)

    out = []
    for _ in range(q):
        t = int(data[idx]); idx += 1
        if t == 1:
            l = int(data[idx]); idx += 1
            r = int(data[idx]); idx += 1
            v = int(data[idx]); idx += 1
            update(1, 1, n, l, r, v)
        else:
            l = int(data[idx]); idx += 1
            r = int(data[idx]); idx += 1
            out.append(str(query(1, 1, n, l, r)))

    print('\n'.join(out))


if __name__ == "__main__":
    main()
