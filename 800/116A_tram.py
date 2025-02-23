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
    on_tram = 0
    curr_max = 0
    n = input_int()
    for _ in range(n):
        a, b = input_multiple_ints()
        on_tram += b - a
        curr_max = max(on_tram, curr_max)
    output(str(curr_max))

if __name__ == "__main__":
    main()