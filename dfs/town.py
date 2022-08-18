# 입력 및 기본 셋팅
n = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# dx, dy technique
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def in_range(x, y):
    if 0 <= x < n and 0 <= y < n: return True
    else : return False

def can_go(x, y):
    if not in_range(x, y): return False

    if visited[x][y] == 1 and grid[x][y] == 0: return False

    return True

def dfs(x, y): 
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if can_go(nx, ny):
            visited[nx][ny] = 1
            dfs(nx, ny)
    return

cnt = 0
for i in range(n):
    for j in range(n):
        if can_go(i, j):
            visited[i][j] = 1
            dfs(i, j)
            cnt += 1

print(cnt)
