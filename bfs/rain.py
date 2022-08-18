import sys
from collections import deque

INT_MAX = sys.maxsize

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

def find_min():
    

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if can_go(nx, ny):
                push(nx, ny, step[x][y] + 1)
    
for s in shelter:
    x, y = s
    push(x, y, 0)

find_min()

for i in range(n):
    for j in range(n):
        if grid[i][j] != 2:
            print(0, end=" ")
        else:
            if not visited[i][j]:
                print(-1, end=" ")
            else:
                print(step[i][j], end=" ")
    print()
