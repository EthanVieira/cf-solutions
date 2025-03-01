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
    line = input_list()
    max_height = max(line)
    max_height_i = line.index(max_height)
    del line[max_height_i]
    line.insert(0, max_height)
    line.reverse()
    min_height_i = line.index(min(line))
    time = max_height_i + min_height_i
    output(str(time))

if __name__ == "__main__":
    main()