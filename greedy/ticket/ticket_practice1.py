def solution(tickets):
    answer = []
    
    trip = {}
    for t in tickets:
        trip[t[0]] = trip.get(t[0], []) + [t[1]]
    
    for t in trip:
        trip[t].sort(reverse = True)
    
    print(trip)
    
    stack = ['ICN']
    path = []
    while len(stack) > 0:
        prev = stack[-1]
        if prev not in trip or trip.get(prev) == []:
            path.append(stack.pop())
        else :
            next = trip[prev][-1]
            stack.append(next)
            trip[prev].pop()
        
    return path[::-1]

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
solution(tickets)