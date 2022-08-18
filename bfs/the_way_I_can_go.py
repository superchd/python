from collections import deque

# 입력받기
n, k = map(int,input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]

start_points = []
for i in range(k):
    start_points.append(map(int, input().split()))

# dx, dy
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not in_range(x, y): return False

    if visited[x][y] == 1 or grid[x][y] == 1 : return False
    
    return True

def bfs(queue):
    global answer

    cnt = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if can_go(nx, ny):
                visited[nx][ny] == 1
                cnt += 1
                queue.append((nx, ny))

    
answer = []
queue = deque()
for i in range(k):
    x, y = start_points[i]
    visited[x][y] = 1
    queue.append((x, y))
    bfs(queue)
print(answer)

