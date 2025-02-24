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
    groups = 1
    pre_mag = 0
    for _ in range(n):
        if pre_mag == 0:
            pre_mag = input_int()
        else:
            mag = input_int()
            if mag != pre_mag:
                groups += 1
            pre_mag = mag

    output(str(groups))

if __name__ == "__main__":
    main()