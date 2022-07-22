def solution(scoville, K):
    answer = 0
    remain = []
    over   = []


    # 데이터 전처리, K보다 작은것과 큰것들을 나눈다
    for s in scoville:
        if s >= K : over.append(s)
        else      : 
            remain.sort(reverse = False)
            remain.append(s)

    # 종료조건, K보다 작은것들이 없으면 종료
    while len(remain) != 0 :
        next   = []
        # K보다 작은원소가 2개보다 클때
        if len(remain) > 2:
            # 음식을 섞는다
            new_food = remain[0] + 2 * remain[1]
            # 제일 앞 두개 원소를 제거한다
            remain.pop(0)
            remain.pop(0)
            # 섞어서 나온 음식을 리스트에 추가하고 정렬한다
            for r in remain:
                next.append(r)
            next.append(new_food)
            next.sort(reverse = False)
        # K보다 작은원소가 2개일때
        elif len(remain) == 2:
            # 음식을 섞는다
            new_food = remain[0] + 2 * remain[1]
            if new_food >= K: return answer + 1
            else : next.append(new_food)
        # K보다 작은원소가 1개일때    
        elif len(remain) == 1:
            # 만들 수 없는 경우
            if remain[0] < K and len(over) == 0:
                return -1
            # K보다 작은원소와 K보다 큰 원소를 섞으면 무조건 그 원소는 K이상
            if remain[0] < K and len(over) > 0 :
                return answer + 1
        remain = next
        print(remain)
        answer += 1

    return answer
