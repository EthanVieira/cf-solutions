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
    s = input_str()
    num_lower = 0
    num_upper = 0
    for c in s:
        if (c.islower()):
            num_lower += 1
        else:
            num_upper += 1
    s = s.lower() if num_lower >= num_upper else s.upper()
    output(s)

if __name__ == "__main__":
    main()