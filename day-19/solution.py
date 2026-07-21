import sys
sys.setrecursionlimit(2000)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def postorder(root, result):
    if root is None:
        return
    postorder(root.left, result)
    postorder(root.right, result)
    result.append(str(root.val))

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    
    n = int(data[idx]); idx += 1
    root = None
    for _ in range(n):
        val = int(data[idx]); idx += 1
        root = insert(root, val)
    
    result = []
    postorder(root, result)
    print(' '.join(result))

if __name__ == "__main__":
    main()
