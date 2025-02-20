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
    s = input_str()
    lucky_count = 0
    for c in s:
        if c == "4" or c == "7":
            lucky_count += 1
    output("YES" if (lucky_count == 4 or lucky_count == 7) else "NO")

if __name__ == "__main__":
    main()