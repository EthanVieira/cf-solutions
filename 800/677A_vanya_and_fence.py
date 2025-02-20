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
    width = 0
    n, h = input_multiple_ints()
    a = input_list()
    for height in a:
        width += 2 if height > h else 1
    output(str(width))

if __name__ == "__main__":
    main()