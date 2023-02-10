def solution(matrix):
    res = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]==0:
                for k in range(i,len(matrix)):
                    matrix[k][j] = 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            res += matrix[i][j]
            
    return res