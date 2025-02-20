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
    new_s = []
    for c in s:
        temp = c.lower()
        if temp not in ["a","e","i","o","u","y"]:
            new_s.append(".")
            new_s.append(temp)
    output("".join(new_s))

if __name__ == "__main__":
    main()