def solution(a):
    for i in range(len(a)):
        min = i
        for j in range(i+1, len(a)):
            if a[i] != -1 and a[j] != -1 and a[min] > a[j]:
                min = j
        tmp = a[i]
        a[i] = a[min]
        a[min] = tmp
    return a