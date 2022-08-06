import copy

def num_check(number, idx, tank, k):
    flag = 0
    tank.append(number[idx])
    temp = copy.deepcopy(tank)

    for i in range(len(temp)):
        if k == 0 : return tank, k
        if len(tank) == 1: return tank, k
    
        if tank[-1] > tank[-2]:
            tank.remove(tank[-2])
            k -= 1
            flag = 1
                
    return tank, k
    
def solution(number, k):
    answer = ''
    tank = []
    idx = 0
    
    while len(number)  != idx and k > 0:
        tank, k = num_check(number, idx, tank, k)
        idx += 1
    
    answer = "".join(tank) + number[idx:]
    
    return answer

number = "4177252841"
k = 4
print(solution(number, k))