def solution(a):
    res = [0]*2
    for i in range(len(a)):
        if(i % 2 == 0):
            res[0] += a[i]
        else:
            res[1] += a[i]
    return res