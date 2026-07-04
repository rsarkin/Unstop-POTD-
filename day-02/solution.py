class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 

def valid_partition(head, x):
    """
    Parameters:
        head (Node): Head of the linked list
        x (int): The partition value
    Returns:
        str: "YES" if the partition point exists, "NO" otherwise
    """
    seen_big = False   # have we seen at least one value >= x so far?
    valid = True         # becomes False if a small value appears after a big one

    current = head
    while current is not None:
        if current.val >= x:
            seen_big = True
        else:
            if seen_big:
                valid = False
        current = current.next

    if valid and seen_big:
        return "YES"
    else:
        return "NO"


def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    x = int(data[1])
    values = list(map(int, data[2:n+2]))
    head = None
    tail = None
    for value in values:
        node = Node(value)
        if head is None:
            head = tail = node
        else:
            tail.next = node
            tail = node
    result = valid_partition(head, x)
    print(result)

if __name__ == "__main__":
   main()
