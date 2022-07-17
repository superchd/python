def solution(people, tshirts):
    
    people.sort()
    tshirts.sort()
    cnt = 0
    for p in people:
        for t in tshirts:
            if p <= t:
                cnt += 1
                tshirts.remove(t)
                break
    answer = cnt
    return answer