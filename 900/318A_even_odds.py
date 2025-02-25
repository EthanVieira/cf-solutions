import sys

input = sys.stdin.readline
output = sys.stdout.write

def input_int():
    return(int(input()))

def input_list():
    return(list(map(int,input().split())))

def input_list_str():
    s = input()
    return(list(s[:len(s) - 1]))

def input_str():
    return input().rstrip()

def input_multiple_ints():
    return(map(int,input().split()))

def main():
    n, k = input_multiple_ints()
    k -= 1
    out = 0
    half = n // 2 if n % 2 == 0 else (n+1)//2
    if k < half:
        out = k *2 + 1
    else:
        out = (k - (half-1)) * 2
    output(str(out))

if __name__ == "__main__":
    main()