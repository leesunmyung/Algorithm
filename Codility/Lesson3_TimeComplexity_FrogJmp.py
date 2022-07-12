# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    return ((Y-X) // D) + (1 if ((Y-X) // D != 0) else 0)