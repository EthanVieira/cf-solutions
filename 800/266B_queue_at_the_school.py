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
    n, t = input_multiple_ints()
    s = input_list_str()
    s2 = "".join(s)
    for _ in range(t):
        for i in range(1, n):
            if s2[i] == 'G' and s2[i-1] == 'B':
                s[i-1] = 'G'
                s[i] = 'B'
        s2 = "".join(s)
    output("".join(s))

if __name__ == "__main__":
    main()