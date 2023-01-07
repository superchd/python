import sys

N, M = map(int, input().split())

a = [
    list(map(int, input().split()))
    for _ in range(N)
]

visited = [
    [False for _ in range(M)]
    for _ in range(N)
]

dxs = [1, 0, -1, 0]
dys = [0, -1, 0, 1]

def in_range(x, y):
    if 0 <= x < N and 0 <= y < M:
        return True
    else : return False

def can_go(x, y, k):
    if in_range(x, y) and not visited[x][y] and a[x][y] > k :
        return True
    else: return False

def dfs(current, path, k):
    x, y = current[0], current[1]

    for dx, dy in zip(dxs, dys):
        current_x, current_y = x + dx, y + dy
        if not can_go(current_x, current_y, k):
            continue
        visited[current_x][current_y] = True
        path.append((current_x, current_y))
        dfs((current_x, current_y), path, k)

mini = -sys.maxsize
max_value = max(map(max, a))
max_idx = 0

for k in range(max_value):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if can_go(i, j, k):
                visited[i][j] = True
                dfs((i, j), [(i, j)], k)
                cnt += 1
    # initialize
    visited = [
        [False for _ in range(M)]
        for _ in range(N)
        ]
    if cnt > mini:
        mini = cnt
        max_idx = k
print(k, mini)
