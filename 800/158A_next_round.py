import sys

input = sys.stdin.readline

def input_multiple_ints():
    return(map(int,input().split()))


if __name__ == "__main__":

    n, k = input_multiple_ints()
    scores = list(input_multiple_ints())

    kth_score = scores[k-1]
    num_advancing = 0

    if kth_score == 0:
        for score in scores:
            if score > kth_score:
                num_advancing += 1
            else:
                break
    else:
        num_advancing = k
        for score in scores[k:]:
            if score == kth_score:
                num_advancing += 1
            else:
                break

    sys.stdout.write(str(num_advancing) + "\n")
