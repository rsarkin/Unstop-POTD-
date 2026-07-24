import sys
sys.setrecursionlimit(3000)

def solve(mask, total, comp, memo):
    if mask == (1 << total) - 1:
        return 0
    if memo[mask] != -1:
        return memo[mask]
    
    # Find the first unpaired guardian (index of the lowest unset bit in mask)
    # Using bitwise: ~mask & (mask + 1) isolates the lowest unset bit as a power of 2.
    first = (~mask & (mask + 1)).bit_length() - 1
    
    best = 0
    for j in range(first + 1, total):
        if not (mask & (1 << j)):
            score = comp[first][j] + solve(mask | (1 << first) | (1 << j), total, comp, memo)
            if score > best:
                best = score
    
    memo[mask] = best
    return best

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    total = 2 * n
    comp = []
    idx = 1
    for i in range(total):
        row = []
        for j in range(total):
            row.append(int(input_data[idx]))
            idx += 1
        comp.append(row)
    
    memo = [-1] * (1 << total)
    print(solve(0, total, comp, memo))

if __name__ == "__main__":
    main()
