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
    a = input_int()
    b = input_int()
    c = input_int()

    out = 0

    if a == 1:
        if b == 1:
            if c == 1:
                out = a + b + c
            else:
                out = (a + b) * c
        elif c == 1:
            out = a + b + c
        else:
            out = (a + b) * c
    elif b == 1:
        if c == 1:
            out = a * (b + c)
        else:
            out = max((b + a) * c, (b + c) * a)
    elif c == 1:
        out = (c + b) * a
    else:
        out = a * b * c

    output(str(out))

if __name__ == "__main__":
    main()