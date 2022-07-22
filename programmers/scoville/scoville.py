answer = 0

def make_food(scoville, K, depth, over):
    global answer

    # 스코빌지수가 k미만인 음식들
    remain =[]
    # 다음 재귀에 들어갈 리스트
    next = []
    
    # 데이터 전처리
    for s in scoville:
        if s < K                  : remain.append(s)
        elif s > K and depth == 0 : over.append(s)
    
    print(remain, over, depth)
    # 종료조건
    if len(remain) == 0: 
        answer = depth
        return depth
    
    # 처음만 정렬하고, 나머지 경우는 정렬할 필요없이 밀어넣자
    if depth == 0: remain.sort(reverse = False)
    print('remain = ', remain)
    # remain의 크기가 2이상일때는, 가장맵지 않은 음식, 그다음 맵지않은 음식을 섞는다
    if len(remain) > 2:
        new_food = remain[0] + remain[1] * 2
    elif len(remain) == 2:
        new_food = remain[0] + remain[1] * 2
        if new_food > K :
            answer = depth + 1 
            return depth + 1
        else : 
            next.append(new_food)
            make_food(next, K, depth + 1, over)
            return
    # remain의 크기가 1일때는, 음식을 한번만 더 섞으면 끝이난다. 
    elif len(remain) == 1:
        return depth + 1
    
    # new_food가 r보다 큰 순간 삽입되므로, 리스트의 정렬이 유지된다.
    for i in range(2, len(remain)):
        print('new_food, remain[i]:', new_food, remain[i])
        if new_food <= remain[i]: 
            next.append(remain[i])
        else:
            next.append(remain[i])
            next.append(new_food)
            new_food = 0

    make_food(next, K, depth + 1, over)

    return

def solution(scoville, K):
    global answer
    make_food(scoville, K, 0, [])
    print(answer)

    return answer
