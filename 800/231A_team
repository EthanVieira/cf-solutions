import sys

input = sys.stdin.readline

def input_int():
    return(int(input()))

def input_multiple_ints():
    return(map(int,input().split()))

if __name__ == "__main__":
    n = input_int()
    num_problems = 0
    for _ in range(n):
        ints = input_multiple_ints()
        if (sum(ints) > 1):
            num_problems += 1

    print(num_problems)