from collections import deque

n, k   = map(int, input().split())

a = [
    input().replace(" ", "")
    for _ in range(n)
]

r1x, r1y = map(int, input().split())
r2x, r2y = map(int, input().split())

dxs = [1, 0, -1, 0]
dys = [0, -1, 0, 1]
count = [
    [0 for _ in range(n + 1)]
    for _ in range(n + 1)
]

visited = [
    [0 for _ in range(n + 1)]
    for _ in range(n + 1)
]

interrupt = [
    [0 for _ in range(n + 1)]
    for _ in range(n + 1)
]

queue = deque()

wall = 0

def in_range(x, y):
    if 1 <= x <= n and 1 <= y <= n: return True
    else : return False

def can_go(x, y):
    if in_range(x, y) and not visited[x][y] and interrupt[x][y] <= k:
        return True
    else : return False

def push(x, y, val, inter):
    global count
    global interrupt
    visited[x][y] = True
    queue.append((x, y))
    count[x][y] = val
    interrupt[x][y] = inter
    #print(f'I m in push, count[{x}][{y}] = {val}' )
    return

flag = False

def bfs():

    global flag
    while queue:
        start = queue.popleft()
        x, y = start[0], start[1]

        if x == r2x and y == r2y and interrupt[x][y] <= k:
            flag = True
            return

        for dx, dy in zip(dxs, dys):
            current_x, current_y = x + dx, y + dy
           
            if can_go(current_x, current_y):
                #print(f'current = {current_x}, {current_y} // {a[current_x - 1][current_y -1]}')
                if a[current_x - 1][current_y - 1] == '1':
                    push(current_x, current_y, count[x][y] + 1, interrupt[x][y] + 1)
                else:
                    push(current_x, current_y, count[x][y] + 1, interrupt[x][y])

queue.append((r1x, r1y))
bfs()
#print(count)
#print(interrupt)
if flag == True:
    print(count[r2x][r2y])
else : print(-1)
