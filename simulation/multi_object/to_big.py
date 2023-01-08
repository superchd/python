import copy

n, m, t = map(int, input().split())

a = [
    list(map(int, input().split()))
    for _ in range(n)
]

points = [
    tuple(map(int, input().split()))
    for _ in range(m)
]

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

count = [
    [0 for _ in range(n)]
    for _ in range(n)
]

new_count = [
    [0 for _ in range(n)]
    for _ in range(n)
]

next_points = copy.deepcopy(points)

def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    else : return False

# make count array
for i in range(len(points)):
    x, y = points[i][0] - 1, points[i][1] - 1
    print(x, y)
    count[x][y] = 1

def move(x, y):
    global new_count
    big_lst = []
    max_num = -1
    max_idx = (x, y)

    for dx, dy in zip(dxs, dys):
        next_x, next_y = x + dx, y + dy
        if in_range(next_x, next_y):
            if a[next_x][next_y] > max_num:    
                max_idx = (next_x, next_y)
                max_num = a[next_x][next_y]
    move_x, move_y = max_idx[0], max_idx[1]
    new_count[move_x][move_y] += 1
            
def process(new_count):
    for i in range(n):
        for j in range(n):
            if new_count[i][j] > 1:
                new_count[i][j] = 0

def find_next_points():
    for i in range(n):
        for j in range(n):
            if new_count[i][j] == 1:
                next_points.append((i, j))

def move_all():
    for i in range(t):
        for p in next_points:
            x, y = p[0] - 1, p[1] - 1
            move(x, y)
            process(new_count)
            find_next_points()
        
move_all()
print(new_count)
//
//
