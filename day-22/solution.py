import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None: return Node(val)
    if val < root.val: root.left = insert(root.left, val)
    else: root.right = insert(root.right, val)
    return root

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    root = None
    for i in range(n):
        val = int(data[idx]); idx += 1
        root = insert(root, val)

    if root is None:
        return

    q = [root]
    front = 0
    out_lines = []
    while front < len(q):
        level_end = len(q)
        level_vals = []
        while front < level_end:
            node = q[front]; front += 1
            level_vals.append(str(node.val))
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        out_lines.append(' '.join(level_vals))

    print('\n'.join(out_lines))

if __name__ == "__main__":
    main()
