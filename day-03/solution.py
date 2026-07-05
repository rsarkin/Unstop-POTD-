class Node:
    def __init__(self, node_id, value, next_id):
        self.node_id = node_id
        self.value = value
        self.next_id = next_id
        self.next = None


def recover_chain(n, node_details, start_id):
    # Step 1: Build all Node objects (dict used only for construction,
    # NOT for cycle detection -- that stays pointer-only, O(1) extra space)
    nodes = {}
    for node_id, value, next_id in node_details:
        nodes[node_id] = Node(node_id, value, next_id)

    for node_id, value, next_id in node_details:
        if next_id != -1:
            nodes[node_id].next = nodes[next_id]

    head = nodes[start_id]

    # Step 2: Floyd's Tortoise and Hare -- detect a cycle
    slow = head
    fast = head
    has_cycle = False

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            has_cycle = True
            break

    # Step 3 & 4: locate the cycle start, then break the link
    if has_cycle:
        slow2 = head
        while slow2 is not slow:
            slow2 = slow2.next
            slow = slow.next
        cycle_start = slow

        temp = cycle_start
        while temp.next is not cycle_start:
            temp = temp.next

        temp.next = None  # cut the repeating link

    # Step 5: traverse the now cycle-free chain
    result = []
    current = head
    while current is not None:
        result.append(current.value)
        current = current.next

    return result


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    if not data or data == ['']:
        return
    n = int(data[0])
    node_details = []
    for i in range(1, n + 1):
        node_id, value, next_id = map(int, data[i].split())
        node_details.append((node_id, value, next_id))
    start_id = int(data[n + 1])
    result = recover_chain(n, node_details, start_id)
    print(' '.join(map(str, result)))  # Step 6: print space-separated

if __name__ == "__main__":
    main()
