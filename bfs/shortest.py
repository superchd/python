from collections import deque

# input
n , m = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]

step = [
    [0 for _ in range(m)]
    for _ in range(n)
]

# dx, dy
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    if not in_range(x, y) : return False

    if visited[x][y] or grid[x][y] == 0: return False

    return True

def push(x, y, s):
    step[x][y] = s
    visited[x][y] = 1
    queue.append((x, y))

def bfs(queue):

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if can_go(nx, ny):
                push(nx, ny, step[x][y] + 1)

queue = deque()
push(0, 0, 0)
queue.append((0, 0))
bfs(queue)

if step[n - 1][m - 1] == 0: print(-1)
else : print(step[n - 1][m - 1])
