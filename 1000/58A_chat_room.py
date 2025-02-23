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
    s = input_list_str()
    hello = "hello"
    result = "NO"
    i = 0
    for c in s:
        if c == hello[i]:
            if (i == 4):
                result = "YES"
                break
            else:
                i += 1

    output(result)

if __name__ == "__main__":
    main()