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
    n1 = input_str()
    n2 = input_str()
    out_s = []
    for i, j in zip(n1, n2):
        if i == j:
            out_s.append("0")
        else:
            out_s.append("1")

    output("".join(out_s))

if __name__ == "__main__":
    main()