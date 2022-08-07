from collections import deque

def dfs(i, j, n, m, graph):
    queue = deque()
    if i <= -1 or i >= n or j <= -1 or j >= m:
        return False

    if graph[i][j] == 0:
        graph[i][j] = 1
        dfs(i + 1, j, n, m, graph)
        dfs(i - 1, j, n, m, graph)
        dfs(i, j + 1, n, m, graph)
        dfs(i, j - 1, n, m, graph)
        return True


def solution():
    n, m = map(int, input().split())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input())))
    # 이미 전 테이블이 나와있기때문에 굳이 i, j 인덱스 값기준으로 테이블을 작성할 필요가 없는것이다. 
    # 순회하자
    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j, n, m, graph) == True:
                result += 1
    print(result)
    return result


solution()