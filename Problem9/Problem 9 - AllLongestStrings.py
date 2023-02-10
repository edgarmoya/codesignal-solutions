def solution(inputArray):
    max_value = max([len(i) for i in inputArray])
    return list(filter(lambda x: len(x) == max_value, inputArray))