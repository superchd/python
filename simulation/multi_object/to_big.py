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

def initial_value():
    for i in range(m):
        first, second = points[i][0] - 1, points[i][1] - 1
        new_count[first][second] = 1 
    count = new_count

def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    else : return False

# make count array
for i in range(len(points)):
    x, y = points[i][0] - 1, points[i][1] - 1
    #print(x, y)
    count[x][y] = 1

def move(x, y):
    big_lst = []
    max_num = -1
    max_idx = (x, y)
    new_count[x][y] = 0
    for dx, dy in zip(dxs, dys):
        next_x, next_y = x + dx, y + dy
        if in_range(next_x, next_y):
            #print('current (x,y) =', x,y, ', next (x,y)', next_x, next_y)
            if a[next_x][next_y] > max_num:    
                max_idx = (next_x, next_y)
                max_num = a[next_x][next_y]
    #print('max_idx', max_idx)
    move_x, move_y = max_idx[0], max_idx[1]
    new_count[move_x][move_y] += 1
    #print(new_count)
            
def process(new_count):
    for i in range(n):
        for j in range(n):
            if new_count[i][j] > 1:
                new_count[i][j] = 0

def simulation():
    for _ in range(t):
        print('------new_count check list---------')
        print(new_count)
        move_all()
        print('------changed----------')
        print(new_count)
        process(new_count)
        count = new_count
       
def move_all():
    for i in range(n):
        for j in range(n):
            if count[i][j] == 1:
                #print('I have to checked', i, j)
                move(i, j)

def count_num():
    ans = 0
    for i in range(n):
        for j in range(n):
            if new_count[i][j] == 1:
                ans += 1
    return ans

initial_value()
simulation()
print(count_num())
