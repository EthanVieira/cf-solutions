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

    for _ in range(k):
        quotient, remainder = divmod(n, 10)
        if (remainder == 0):
            n = quotient
        else:
            n -= 1

    output(str(n))

if __name__ == "__main__":
    main()