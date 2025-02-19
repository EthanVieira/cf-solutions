import sys
import math

input = sys.stdin.readline

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
    n, m, a = input_multiple_ints()
    num_n = math.ceil(n/a)
    num_m = math.ceil(m/a)
    sys.stdout.write(str(num_n*num_m))

if __name__ == "__main__":
    main()