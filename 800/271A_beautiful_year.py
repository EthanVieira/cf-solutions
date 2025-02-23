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

def hasDistinctDigits(y) -> bool:
    digits = list(str(y))
    return len(digits) == len(set(digits))

def main():
    y = input_int()
    y += 1
    while (not hasDistinctDigits(y)):
        y += 1

    output(str(y))

if __name__ == "__main__":
    main()