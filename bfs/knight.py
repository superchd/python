from collections import deque
import sys

INT_MAX = sys.maxsize

# input and initial condition
n = int(input())

visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]

step = [
    [0 for _ in range(n)]
    for _ in range(n)
]

r1, c1, r2, c2 = map(int, input().split())
start = (r1, c1)
end = (r2, c2)

q = deque()
ans = INT_MAX
# dx, dy
dx = [2, 1, -1, -2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    return in_range(x, y) and not visited[x][y]

def push(x, y, s):
    visited[x][y] = 1
    q.append((x, y))
    step[x][y] = s

def find_min():
    global ans
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if can_go(nx, ny):
                push(nx, ny, step[x][y] + 1)

    if visited[r2 - 1][c2 - 1]:
        ans = step[r2 - 1][c2 - 1]

push(r1 - 1, c1 - 1, 0)
find_min()

if ans == INT_MAX:
    ans = -1
print(ans)
