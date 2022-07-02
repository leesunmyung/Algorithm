# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    unique_value = []

    for i in range(0, len(A)):
        if (A.count(A[i]) == 1):
            unique_value.append(A[i])

    return unique_value[0] if (unique_value) else -1
