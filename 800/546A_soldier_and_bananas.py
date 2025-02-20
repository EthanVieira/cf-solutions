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
    k, n, w = input_multiple_ints()

    price = sum(i*k for i in range(1, w+1))
    loan = 0
    if (price > n):
        loan = price - n
    output(str(loan))

if __name__ == "__main__":
    main()