import sys
from collections import deque

INT_MAX = sys.maxsize
ans = INT_MAX
# input and initial condition
n, h, m = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# minimal distance to arrive
step = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# answer
dist = [
    [0 for _ in range(n)]
    for _ in range(n)
] 

# dx, dy
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# my queue
q = deque()

# can_go condition
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and grid[x][y] != 1

def push(x, y, s):
    visited[x][y] = 1
    q.append((x, y))
    step[x][y] = s

# 사람이 어디어디 있는지 찾기
humans = []
def find_human():
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 2:
                humans.append((i, j)) 

# 쉼터가 어디어디 있는지 찾기
shelter = []
def find_shelter():
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 3:
                shelter.append((i, j))

# 사람위치랑 쉼터위치랑 확인해놓기
find_human()
find_shelter()

def find_min(start_x, start_y):
    dist[start_x][start_y] = INT_MAX

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if can_go(nx, ny):
                push(nx, ny, step[x][y] + 1)

    # 도착점까지 얼마나 먼가
    for s in shelter:
        end_x, end_y = s
        if visited[end_x][end_y]:
            dist[start_x][start_y] = min(dist[start_x][start_y], step[end_x][end_y])
        
    
for i in range(h):
    x, y = humans[i]
    push(x, y, 0)
    find_min(x, y)
    visited = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]

for i in range(n):
    for j in range(n):
        if dist[i][j] == INT_MAX:
            dist[i][j] = -1

for d in dist:
    print(*d)
