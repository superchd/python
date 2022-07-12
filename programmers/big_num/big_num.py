import copy

ans = []

def dfs(depth, next, unvisited):
    global ans
    print(f'depth = {depth}, next = {next}')
    if len(unvisited) == 0:
        ans.append(next)
        
    temp = copy.deepcopy(unvisited)
    
    for u in unvisited:
        temp.remove(u)
        dfs(depth + 1, next + str(u), temp)
        temp.append(u)
    return

def solution(numbers):
    global ans
    
    dfs(0, '', numbers)
    print(ans)
    
    return max(ans)
