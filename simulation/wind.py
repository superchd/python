N, M, Q = map(int, input().split())

a = [
    list(map(int, input().split()))
    for _ in range(N)
]

wind = [
    input()
    for _ in range(Q)
]

# 바람이 불때 영향받는 층들을 구하기
floor, direction = wind[0]
# 0층은 없고 1층부터 시작한다~
floor = int(floor) - 1

# dx, dy 테크닉
dy = [-1, 1]

# 유효한 층인지 체크
def in_range(floor):
    return 0 <= floor < M
    
# 바람에 영향을 받는지 체크
def is_affect(floor, ny):
    for i in range(M):
        if a[floor][i] == a[ny][i]:
            return True
    return False

# 왼쪽으로 밀거나, 오른쪽으로 밀거나
def shift(d, ny):
    if d = 'R': 
        temp = a[ny][n - 1]
        for i in range(n - 1, 0, -1):
            a[ny][i] = a[ny][i - 1]
            a[ny][0] = temp
    else:
        temp = a[ny][0]
        for i in range(0, n - 1):
            a[ny][i] = a[ny][i + 1]
            a[ny][n - 1] = temp
        
# 영향을 받아 움직일 층과 바람을 정면으로 받은 층 고르기
affected = [floor]
for i in range(2):
    ny = floor + dy[i]
    if in_range(ny):
        if is_affect(floor, ny) : affected.append(ny)
        
# 층을 골랐으니 이제 shift 해보자
for move_floor in affected:
    shift(direction, move_floor)

