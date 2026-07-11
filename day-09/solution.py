def top_record(ops):
    """
    Simulates a stack of records based on the given operations.

    Parameters:
        ops (list): List of tuples representing operations.
                    e.g., [("ADD", "10"), ("REMOVE",)]

    Returns:
        int: The value of the record visible at the top after all operations,
             or -1 if the pile is empty.
    """
    stk = []
    for op in ops:
        if op[0] == "ADD":
            stk.append(int(op[1]))
        elif op[0] == "REMOVE":
            if stk:
                stk.pop()
    return stk[-1] if stk else -1


def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    n = int(data[idx])
    idx += 1

    ops = []
    for _ in range(n):
        if idx >= len(data):
            break
        if data[idx] == "ADD":
            if idx + 1 < len(data):
                ops.append(("ADD", data[idx + 1]))
                idx += 2
            else:
                idx += 1
        else:
            ops.append(("REMOVE",))
            idx += 1

    print(top_record(ops))


if __name__ == "__main__":
    main()
