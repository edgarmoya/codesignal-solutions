def solution(s1, s2):
    res = 0
    for p1 in s1:
        if p1 in s2:
            s2 = s2.replace(p1, '', 1)
            res += 1
            
    return res