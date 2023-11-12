import sys

input = sys.stdin.readline

def input_int():
    return(int(input()))

def input_str():
    s = input()
    return(list(s[:len(s) - 1]))

if __name__ == "__main__":
    n = input_int()

    value = 0

    for _ in range(n):
        s = input_str()
        if '+' in s:
            value += 1
        else:
            value -= 1

    sys.stdout.write(str(value) + "\n")