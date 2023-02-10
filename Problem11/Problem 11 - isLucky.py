def solution(n):
    numbers = list(map(int, list(str(n))))
    length = len(str(n))
    s1 = sum(numbers[0:(length//2)])
    s2 = sum(numbers[length//2:length])
    
    return s1 == s2