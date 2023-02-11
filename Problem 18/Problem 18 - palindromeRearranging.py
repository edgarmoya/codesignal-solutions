def solution(inputString):
    return sum([inputString.count(i)%2 for i in set(inputString)]) <= 1