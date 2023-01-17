n = int(input())

x, y = map(int, input().split())

a = [
    input()
    for _ in range(n)
]

visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]

start = (x - 1, y - 1)

# right, down, left, up
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

direction = ['우', '아래', '좌', '상']

# 방향전환 시그널 
dic = {}
dic[0] = (1, -1)
dic[1] = (-1, -1)
dic[2] = (-1, 1)
dic[3] = (1, 1)

# 방향전환하자
convert = {}
convert[0] = 1
convert[1] = 2
convert[2] = 3
convert[3] = 0

x, y = start[0], start[1]

def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    else: return False

def can_go(x, y):
    if in_range(x, y) and a[x][y] == '.' and not visited[x][y]: 
        return True
    else: return False

def lets_change(x, y, cur_dir):
    x, y = x + dic[cur_dir][0], y + dic[cur_dir][1]
    if a[x][y] == '#':
        return True
    return False

def move(x, y, cur_dir):
    for i in range(4):
        # 일단, 방향전환을 해야하는지 확인
        if lets_change(x, y, cur_dir):
            next_dir = convert[cur_dir]
        else :
            next_dir = (cur_dir + i) % 4

        current_x, current_y = x + dx[next_dir], y + dy[next_dir]
        if can_go(current_x, current_y):
            x, y = current_x, current_y
            visited[x][y] = True
            return x, y, next_dir
    return -1, -1, -1

cnt = 0
possible = 1
# 처음시작은 오른쪽으로 간다.
cur_dir = 0

while(cur_dir != -1):
    print(f'현재 좌표: ({x}, {y}), 현재 방향: {direction[cur_dir]}')
    x, y, cur_dir = move(x, y, cur_dir)
    print('----------changed-------------')
    print(x, y, direction[cur_dir])
    cnt += 1

print(cnt)
