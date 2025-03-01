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
    k = input_int()
    l = input_int()
    m = input_int()
    n = input_int()
    d = input_int()

    nums = [k, l, m, n]
    drags = set()

    if any(num == 1 for num in nums):
        output(str(d))
    else:
        for num in nums:
            new_num = num
            while new_num <= d:
                drags.add(new_num)
                new_num += num

        output(str(len(drags)))

if __name__ == "__main__":
    main()