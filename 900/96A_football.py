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
    prev_c = ""
    count = 0

    for c in s:
        if c == prev_c:
            count += 1
            if (count >= 7):
                output("YES")
                return
        else:
            count = 1
            prev_c = c

    output("NO")

if __name__ == "__main__":
    main()