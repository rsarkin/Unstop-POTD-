import sys
import math

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    
    A = int(data[idx]); idx += 1
    B = int(data[idx]); idx += 1
    
    # LCM = (A * B) / GCD(A, B)
    g = math.gcd(A, B)
    lcm = (A * B) // g
    
    print(lcm)

if __name__ == "__main__":
    main()
