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
    s = input().rstrip()
    s2 = s.split("+");
    s2.sort();
    sys.stdout.write("+".join(s2));

if __name__ == "__main__":
    main()