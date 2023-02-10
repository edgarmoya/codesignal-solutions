def solution(inputString):
    rev = inputString[::-1]
    
    for i in range(len(inputString)): 
        if inputString[i] != rev[i]:
            return False
    return True