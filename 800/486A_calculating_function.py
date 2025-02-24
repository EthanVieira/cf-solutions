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
    s = 0
    if (n % 2 == 0):
        s = n // 2
    else:
        s = ((n + 1) // 2) * -1

    output(str(s))

if __name__ == "__main__":
    main()