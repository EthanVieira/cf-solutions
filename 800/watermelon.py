import sys

input = sys.stdin.readline

def input_int():
    return(int(input()))

if __name__ == "__main__":
    size = input_int()
    print("YES" if ((size % 2) == 0 and size > 2) else "NO")
