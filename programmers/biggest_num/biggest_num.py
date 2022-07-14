from queue import Queue

def solution(number, k):
    answer = ''
    
    # queue 만들기 
    Q = []
    final_Q = Queue()
    for i in range(10):
        q = Queue()
        Q.append(q)
    
    # 문자열 전처리하기 (case3 처럼 제일 앞 두수를 제거하는경우)
    idx = 0
    max = 0
    for i in range(k):
        if max < int(number[i]):
            max = int(number[i])
            idx = i
            
    # 제거할 문자열의 인덱스를 스페이스로 치환
    N = list(number)
    for i in range(idx):
        N[i] = " "
        k -= 1
        
    number = "".join(N)
    
    number = number.replace(" ", "")
    print(number, k)
        
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
