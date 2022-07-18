from queue import Queue

def num_check(number, idx, tank, k):
    for i in range(len(tank)):
        if tank[i] < number[idx] and k > 0:
            del tank[i]
            k += 1

    return tank, k

def solution(number, k):
    answer = ''
    Q = Queue()
    tank = []
    idx = 0
    
    while len(number) - 1 != idx and k > 0:
        tank, k = num_check(number, idx, tank, k)
        idx += 1
    

    
    return answer
