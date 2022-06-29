# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(E, L):
    enter_hr = int(E.split(':')[0])
    enter_min = int(E.split(':')[1])
    left_hr = int(L.split(':')[0])
    left_min = int(L.split(':')[1])

    # default cost
    cost = 2

    # flag for the first full of partial hour cost
    first = 1

    for i in range(enter_hr+1, left_hr+1):
        if (first == 1):
            cost += 3
            first = 0
            continue
        cost += 4


    if (enter_min < left_min):
        if (first == 1):
            cost += 3
        else:
            cost += 4
    
    return cost
