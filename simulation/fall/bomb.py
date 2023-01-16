n = int(input())

a = [
    list(map(int, input().split()))
    for _ in range(n)
]

temp = [
    [0 for _ in range(n)]
    for _ in range(n)
]

r, c = map(int, input().split())

r, c = r - 1 , c - 1

BLANK = 0

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

size = a[r][c]

def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    else : return False
# Bomb
for s in range(size):
    for i in range(4):
        current_x, current_y = r + s * dx[i], c + s * dy[i]
        if in_range(current_x, current_y):
            a[current_x][current_y] = 0

# Falling
for j in range(n):
    temp_raw = n - 1
    for raw in range(n - 1, -1, -1):
        if a[raw][j] != 0:
            temp[temp_raw][j] = a[raw][j]
            temp_raw -= 1
        
for i in range(n):
    for j in range(n):
        print(temp[i][j], end = ' ')
    print()


