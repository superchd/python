N, M = map(int, input().split())

a = [
    list(map(int, input().split()))
    for _ in range(N)
]

visited = [
    [False for _ in range(M)]
    for _ in range(N)
]

cnt = 0

dxs = [1, 0, -1, 0]
dys = [0, -1, 0, 1]

def in_range(x, y):
    if 0 <= x < N and 0 <= y < M:
        return True
    else : return False

def can_go(x, y, k):
    if in_range(x, y) and not visited[x][y] and a[x][y] > k :
        return True

def is_blocked(x, y, k):
    for dx, dy in zip(dxs, dys):
        current_x, current_y = x + dx, y + dy
        if can_go(current_x, current_y, k):
            return False

    return True

def dfs(current, path, k):
    global cnt
    x, y = current[0], current[1]
    if is_blocked(x, y, k):
#        print(path 
        cnt += 1
        return

    for dx, dy in zip(dxs, dys):
        current_x, current_y = x + dx, y + dy
        if not can_go(current_x, current_y, k):
            continue
        visited[current_x][current_y] = True
        path.append((current_x, current_y))
        dfs((current_x, current_y), path, k)
        visited[current_x][current_y] = False
        path.pop(-1)

cnt = 0
for i in range(N):
    for j in range(M):
        if can_go(i, j, 1):
            dfs((i, j), [], 1)
            
print(cnt)
