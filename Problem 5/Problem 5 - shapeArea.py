def solution(n):
    res, multi = 0, 1
    for i in range(1,n+1):
        res += multi * 2
        if i != n: multi += 2
    res -= multi  
    return res