# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    K = 0

    while (N % pow(2, K) == 0):
        K += 1

    K -= 1
    
    return K
