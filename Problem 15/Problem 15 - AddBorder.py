def solution(picture):
    length = len(picture)+2
    asterisk = len(picture[0])+2
    count = 0
    res = []
    for i in range(length):
        if i == 0 or i == length-1:
            res.append('*'*asterisk)
        else:
            res.append('*' +picture[count]+ '*')
            count += 1       
    return res