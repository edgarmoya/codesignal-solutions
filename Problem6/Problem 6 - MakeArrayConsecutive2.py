
def solution(statues):
    ans = 0
    # search min and max
    results_list = sorted(statues)
    min, max = results_list[0], results_list[-1]
    
    for i in range(min, max):
        min += 1
        if min not in statues:
            ans += 1
    return ans
