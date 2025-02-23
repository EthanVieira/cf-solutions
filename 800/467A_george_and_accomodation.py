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
    n = input_int()
    total = 0
    for _ in range(n):
        p, q = input_multiple_ints()
        if (q - p >= 2):
            total += 1

    output(str(total))

if __name__ == "__main__":
    main()