import sys

input = sys.stdin.readline

def input_int():
    return(int(input()))

def input_list():
    return(list(map(int,input().split())))

def input_str():
    s = input()
    return(list(s[:len(s) - 1]))

def input_multiplie_ints():
    return(map(int,input().split()))