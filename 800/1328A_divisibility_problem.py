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
    t = input_int()
    outs = []
    for _ in range(t):
        a, b = input_multiple_ints()
        a_mod_b = a % b
        outs.append(0 if a_mod_b == 0 else b - a_mod_b)

    for out in outs:
        output(str(out) + "\n")

if __name__ == "__main__":
    main()