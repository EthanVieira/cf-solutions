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
    x_sum = 0
    y_sum = 0
    z_sum = 0
    for _ in range(n):
        x, y, z = input_multiple_ints()
        x_sum += x
        y_sum += y
        z_sum += z

    output("YES" if (x_sum == 0 and y_sum == 0 and z_sum == 0) else "NO")

if __name__ == "__main__":
    main()