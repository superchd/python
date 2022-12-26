from collections import deque

# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))

a = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

dxs = [1, 0, -1, 0]
dys = [0, -1, 0, 1]

def in_range(x, y):
    if 0 <= x <= n - 1 and 0 <= y <= m - 1: return True
    else: return False

def can_go(x, y):
    if a[x][y] == 1 and not visited[x][y]: return True
    else: return False

def push(x, y):
    visited[x][y] = True
    queue.append((x, y))

queue = deque([(0, 0)])

while queue:
    curr_v = queue.popleft()
    x, y = curr_v[0], curr_v[1]
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy
        if in_range(new_x, new_y) and can_go(new_x, new_y):
            push(new_x, new_y)

if visited[n - 1][m - 1] == 1: print(1)
else : print(0)
