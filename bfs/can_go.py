from collections import deque

# 변수 선언 및 입력:
n, k = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
    ]

points = []
for _ in range(k):
    points.append(tuple(map(int, input().split())))

def in_range(x, y):
    if 1 <= x <= n  and 1 <= y <= n : return True
    else : return False

def can_go(x, y):
    if grid[x - 1][y - 1] == 0 and not visited[x - 1][y - 1]:
        return True
    else : return False

'''
def push(x, y):
    visited[x - 1][y - 1] = True
    queue.append((x, y))
'''

dxs = [1, 0, -1, 0]
dys = [0, -1, 0, 1]

def bfs(x, y):
    queue = deque([(x, y)])
    while queue:
        curr_v = queue.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy
            if in_range(new_x, new_y) and can_go(new_x, new_y):
                visited[x - 1][y - 1] = True
                queue.append((x, y))

for i in range(k):
    x, y = points[i][0], points[i][1]
    bfs(x, y)

cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 1:
            cnt += 1

print(cnt)
