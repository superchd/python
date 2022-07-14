from queue import Queue

def solution(number, k):
    answer = ''
    
    # queue 만들기 
    Q = []
    final_Q = Queue()
    for i in range(10):
        q = Queue()
        Q.append(q)
                
    # 처음으로 가장 큰 수가 나올 때, 그 수의 인덱스 찾기
    max = 0
    idx = 0
    for i in range(len(number)): 
        if max < int(number[i]):
            max = int(number[i])
            idx = i
   
    # number문자열을 가공한다. number중에 제일 큰 수가 제일 앞에 오도록!
    if idx + 1 < k:
        number = number[idx:]
        k = k - idx
    print(k, idx, number)
        
    # queue로 숫자의 인덱스를 집어넣는다 
    for i in range(len(number)):
        Q[int(number[i])].put(i)
    
    # final_Q에 0, 1, 2, 3... 순서대로 인덱스를 집어넣는다.
    for i in range(10):
        while Q[i].qsize() > 0:
            final_Q.put(Q[i].get())
            
    # 제거할 문자열의 인덱스를 스페이스로 치환
    N = list(number)
    while k > 0:
        idx = final_Q.get() 
        N[idx] = ' '
        k -= 1
    
    answer = "".join(N)
    
    answer = answer.replace(" ", "")
            
    return answer
