from queue import Queue

def dfs(depth, Q, numbers):
    next = []
    
    if depth == 3:
        print(numbers)
        return
    
    for n in numbers:
        r = int(n[2 - depth]) % 10
        Q[r].put(n)
    
    print(Q)
    for r in range(10):
        while Q[r].qsize() > 0:
            next.append(Q[r].get())
        
    dfs(depth + 1, Q, next)
    return    
    

def solution(numbers):
    # process numbers to compare 
    numbers = list(map(str, numbers))
    for i in range(len(numbers)):
        numbers[i] = numbers[i] * 3
    
    # make 10 queues
    Q = []
    for i in range(10):
        q = Queue()
        Q.append(q)
    #print(Q)
    dfs(0, Q, numbers)
        
    #return answer

numbers = [3, 30, 34, 5, 9]	
solution(numbers)