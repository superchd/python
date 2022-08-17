# 입력받기
n, t = map(int, input().split())

r, c, dir = input().split()
r = int(r) - 1
c = int(c) - 1

# dx, dy 테크닉
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]
nx , ny = r, c

# 방향잡기
direction = {'R': 0, 'D':1, 'U':2, 'L':3} 
dir_num = direction[dir]

def in_range(x, y, n):
    if 0 <= x < n and 0 <= y < n : return True
    else: return False

# 시뮬레이션
for _ in range(t):
    temp1, temp2 = nx, ny
    nx, ny = nx + dx[dir_num] , ny + dy[dir_num]
    if in_range(nx, ny, n) == False:
        dir_num = 3 - dir_num
        nx, ny = temp1, temp2
        continue
print(nx + 1, ny + 1)
