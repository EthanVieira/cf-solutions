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
    ns = input_list()
    s = sum(ns)
    my_sum = 0
    ns.sort(reverse=True)
    i = 0
    while my_sum <= (s/2):
        my_sum += ns[i]
        i += 1
    output(str(i))

if __name__ == "__main__":
    main()