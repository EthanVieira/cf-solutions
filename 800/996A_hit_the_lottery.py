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

    hundreds, remainder = divmod(n, 100)
    twenties, remainder = divmod(remainder, 20)
    tens, remainder = divmod(remainder, 10)
    fives, remainder = divmod(remainder, 5)

    output(str(hundreds + twenties + tens + fives + remainder))

if __name__ == "__main__":
    main()