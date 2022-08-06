from queue import Queue
dict = {}
ans = []
def dfs(depth, Q, numbers):
    next = []
    global ans
    global dict
    if depth == 3:
        for i in range(len(numbers) - 1, -1, -1):
            ans.append(dict.get(numbers[i]))
        return
    
    for n in numbers:
        r = int(n[len(n) - 1 - depth]) % 10
        Q[r].put(n)
    
    for r in range(10):
        while Q[r].qsize() > 0:
            next.append(Q[r].get())
        
    dfs(depth + 1, Q, next)
    return    
    

def solution(numbers):
    # process numbers to compare 
    numbers = list(map(str, numbers))
    global dict
    global ans
    for i in range(len(numbers)):
        dict[numbers[i] * 3] = numbers[i]
        numbers[i] = numbers[i] * 3
    print(dict)
    
    # make 10 queues
    Q = []
    for i in range(10):
        q = Queue()
        Q.append(q)
    #print(Q)
    dfs(0, Q, numbers)
    return(str(int(''.join(ans))))
