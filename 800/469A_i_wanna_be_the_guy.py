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

    ps = set(input_list()[1:])
    qs = set(input_list()[1:])
    output("I become the guy." if len(ps.union(qs)) == n else "Oh, my keyboard!")

if __name__ == "__main__":
    main()