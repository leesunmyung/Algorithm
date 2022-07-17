# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    min_diff = 0
    diff = 0

    first = 1
    for i in range(1, len(A)):
        diff = abs(sum(A[0:i]) - sum(A[i:]))

        if (first == 1):
            min_diff = diff
            first = 0
            continue

        min_diff = diff if (diff <= min_diff) else min_diff

    return min_diff
