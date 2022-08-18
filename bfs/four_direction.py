from collections import deque
# 입력받기 및 그래프 셋팅

n, m = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]

# dx, dy technique
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def in_range(x, y):
    if 0 <= x < n and 0 <= y < m: return True
    else : return False

def can_go(x, y):
    if not in_range(x, y) : return False

    if visited[x][y] == 1 or grid[x][y] == 0: return False

    return True

def bfs(queue):

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if can_go(nx, ny):
                visited[nx][ny] = 1
                #print(nx, ny)
                queue.append((nx, ny))

queue = deque()
queue.append((0, 0))
visited[0][0] = 1
bfs(queue)

print(visited[n - 1][m - 1])
