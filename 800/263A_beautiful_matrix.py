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

    for i in range(5):
        ints = list(input_multiple_ints())
        for j in range(5):
            if (ints[j] == 1):
                num_moves = abs(i - 2) + abs(j - 2)
                sys.stdout.write(str(num_moves) + "\n")
                return;
    

if __name__ == "__main__":
    main()