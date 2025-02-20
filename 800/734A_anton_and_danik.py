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
    s = input_str()
    a_count = 0
    d_count = 0
    for c in s:
        if c == "A":
            a_count += 1
        else:
            d_count += 1

    out = ""
    if a_count == d_count:
        out = "Friendship"
    elif a_count > d_count:
        out = "Anton"
    else:
        out = "Danik"

    output(out)

if __name__ == "__main__":
    main()