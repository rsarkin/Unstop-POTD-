import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    q = []
    front = 0
    for _ in range(n):
        if idx >= len(data):
            break
        event = data[idx]; idx += 1
        if event == "ENTER":
            if idx < len(data):
                x = data[idx]; idx += 1
                q.append(x)
        elif event == "EXIT":
            if front < len(q):
                front += 1
    print(q[front] if front < len(q) else "EMPTY")

if __name__ == "__main__":
    main()
