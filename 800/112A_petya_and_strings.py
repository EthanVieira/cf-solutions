import sys

input = sys.stdin.readline

def input_int():
    return(int(input()))

def input_int_list():
    return(list(map(int,input().split())))

def input_str():
    s = input()
    return(list(s[:len(s) - 1]))

def input_multiple_ints():
    return(map(int,input().split()))

def main():
    s1 = input().lower()
    s2 = input().lower()

    if (s1 > s2):
        print(1)
    elif (s1 < s2):
        print(-1)
    else:
        print(0)

if __name__ == "__main__":
    main()