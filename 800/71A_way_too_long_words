import sys

input = sys.stdin.readline

def input_int():
    return(int(input()))

def input_str():
    s = input()
    return(list(s[:len(s) - 1]))

if __name__ == "__main__":
    n = input_int()
    for _ in range(n):
        s = input_str()
        length = len(s)
        if length > 10:
             print(s[0] + str(length - 2) + s[-1])
        else:   
            print(''.join(s))