from collections import deque

def bfs(graph, x, y, queue):
    global n
    global m

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    depth = 0

    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]
            if nx == n - 1 and ny == m - 1: 
                print(depth)
                return depth
            # 확인할 네모칸이 범위 밖이면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >=m :
                continue    
            # 이미 네모칸을 방문했다면 무시
            if visited[nx][ny] == 1:
                continue
            if graph[nx][ny] == 1:
                queue.append([nx, ny])
                visited[nx][ny] = 1
                depth += 1
    
    pass

def solution():
    global n
    global m
    global visited
    n, m = map(int, input().split())

    graph = []
    for i in range(n):
        graph.append(list(map(int, input())))
    # 이미 전 테이블이 나와있기때문에 굳이 i, j 인덱스 값기준으로 테이블을 작성할 필요가 없는것이다. 
    # 순회하자
    visited = [[0] * m for _ in range(n)]
    queue = deque()
    queue.append([1, 1])
    visited[1][1] = 1
    bfs(graph, 1, 1, queue)
    return

solution()