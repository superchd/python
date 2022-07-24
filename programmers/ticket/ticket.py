# 딕셔너리 val를 중복으로 허용해주겠다
class ticket(object):
    def __init__(self, depart):
        self.depart = depart
    # 클래스니까 출력 포맷을 정한다.
    def __str__(self):
        return self.depart
    def __repr__(self):
        return "'" + self.depart + "'"

def pre_process(tickets):
    data = {}

    for t in tickets:
        data[ticket(t[0])] = t[1]
    return data

# 처음 출발점을 알아할거 같은데
def my_sol(data):

    # key값들만 뽑아내고, value값들만 뽑아낸다.
    key = data.keys()
    val = data.values()
    first = ''
    arrive = ''
    print(key, val)
    print(data)

    # 제일 처음 출발하는 도시를 찾는다.(dict[key]했을 때, val가 없으면 출발하는 도시)
    for v in val:
        if data.get(ticket(v)) == None:
            print(f"v = {v}, get(v) = {data.get(v)}")
            first = v
            break

    # 여행 마지막 도시를 찾는다.
    for k in key:
        
        if data.get(k) == None:
            arrive = k
            break

    print(first)
    return 

def solution(tickets):
    answer = []
    data = pre_process(tickets)
    my_sol(data)
    return answer
