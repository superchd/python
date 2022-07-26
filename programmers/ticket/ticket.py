def solution(tickets):
    answer = []
    routes = {}
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
        
    for r in routes:
        routes[r].sort(reverse = True)
        
    stack = ['ICN']
    
    # 종료조건 어떻게 설정할지 모르겠고
    
    path = []
    
    while len(stack) > 0:
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else : 
            stack.append(routes[top][-1])
            routes[top].pop()
    return path[::-1]
        
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

solution(tickets)