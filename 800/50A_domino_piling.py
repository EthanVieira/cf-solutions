import sys

input = sys.stdin.readline

def input_int():
    return(int(input()))

def input_list():
    return(list(map(int,input().split())))

def input_str():
    s = input()
    return(list(s[:len(s) - 1]))

def input_multiple_ints():
    return(map(int,input().split()))

def main():
    m, n = input_multiple_ints()
    sys.stdout.write(str((m*n)//2) + "\n")


if __name__ == "__main__":
    main()