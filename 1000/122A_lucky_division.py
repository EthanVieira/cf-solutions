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
    lucky_ns = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 777]
    response = "NO"
    for lucky in lucky_ns:
        if n % lucky == 0:
            response = "YES"
            break
    output(response)

if __name__ == "__main__":
    main()