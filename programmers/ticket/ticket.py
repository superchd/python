# 키 중복을 처리하기 위한 딕셔너리를 만든다
def pre_process(tickets):
    data = {}

    for t in tickets:
        ex = []

        if data.get(t[0]) == None:
            data[t[0]] = t[1]
        else :
            if type(data[t[0]]) == str:
                ex.append(data[t[0]])
                ex.append(t[1])
                data[t[0]] = ex
            else :
                for d in data[t[0]]:
                    ex.append(d)
                    ex.append(d[1])
                    data[t[0]] = ex 

    return data



# 처음 출발점을 알아할거 같은데
def my_sol(data):

    # key값들만 뽑아내고, value값들만 뽑아낸다.
    key = data.keys()
    val = data.values()
    first = ''
    arrive = ''
    print(key, val)

    # 제일 처음 출발하는 도시를 찾는다.(dict[key]했을 때, val가 없으면 출발하는 도시)
    for v in val:
        for ele in v:
            if ele in data == True:
                first = v
                break

    # 여행 마지막 도시를 찾는다.
    for k in key:
        if data.get(k) == None:
            arrive = k
            break

    print(first, arrive)

    return 

def solution(tickets):
    answer = []
    data = pre_process(tickets)
    my_sol(data)
    return answer
