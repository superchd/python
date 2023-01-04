N, M = map(int, input().split())

a = [
    list(map(int, input().split))
    for _ in range(N)
]

visited = [
    [False for _ in range(M + 1)]
    for _ in range(N + 1)
]

cnt = 0

dxs = [1, 0, -1, 0]
dys = [0, -1, 0, 1]

def dfs(current, path):
    
    if end_condition:
        pass

    for dx, dy in zip(dxs, dys):
        current_x, current_y = x + dx, y + dy
        if can_go(current_x, current_y):
            visited[current_x][current_y] = True
            path.append((current_x, current_y))
            dfs
