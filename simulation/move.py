n, r, c = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

dxs = [0, 0, -1, 1]
dys = [-1, 1, 0, 0]

def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    else : return False

def move(x, y):
    num = grid[x][y]
    table = []
    for i in range(4):
        print(dxs[i], dys[i])
        current_x, current_y = x + dxs[i], y + dys[i]
        if in_range(current_x, current_y):
            if grid[current_x][current_y] > num:
                table.append((current_x, current_y))
        
    print(table)
    if len(table) == 0: 
        return -1, -1

    else: return table[0][0], table[0][1]

r -= 1
c -= 1
while r != -1 and c != -1:
    last_r, last_c = r, c
    print(r, c, grid[r][c])
    r , c = move(r, c)
    
print('--------------------------------')
print(last_r, last_c)

