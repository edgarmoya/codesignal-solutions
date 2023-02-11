def solution(a, b):
    change = -1
    count = 0
    for i in range(len(a)):
        if a[i] != b[i] and change != -1:
            if a[change]!=b[i] or b[change]!=a[i]:
                return False
                
        if a[i] != b[i] and change == -1:
            change = i
        
        if a[i] == b[i]:
            count += 1      
            
    return len(a)-2 == count or len(a) == count