# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):

    binary_num = bin(N)[2:]

    flag = 0
    binary_gaps = []
    binary_gap = 0

    for i in range(0, len(binary_num)):

        if (flag == 1) and (binary_num[i] == '0'):
            binary_gap += 1
        
        if (flag == 1) and (binary_num[i] == '1'):
            binary_gaps.append(binary_gap)
            binary_gap = 0
            flag = 0

        if (i != len(binary_num)-1) and (binary_num[i] == '1') and (binary_num[i+1] == '0'):
            flag = 1
            continue

    return 0 if len(binary_gaps) == 0 else max(binary_gaps)

