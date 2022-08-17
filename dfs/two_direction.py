# input and draw grid
n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

visited = [False * m for _ in range(n)]

# dx, dy technique
dx = [1, 0]
dy = [0, 1]
nx, ny = 0, 0

# can_go condition
def in_range(x, y):
    if 0 <= x < n and 0 <= y < m: return True
    else: return False

def can_go(x, y):
    if in_range(x, y) and grid[x][y] == 1:
        return True
    else : return False

def dfs(x, y):
    if x == n - 1 and y == m - 1:
        print('1')
        return 

    nx , ny = x, y
    for i in range(2):
        nx, ny = nx + dx[i], ny + dy[i]
        if can_go(nx, ny) and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny)
            visited[nx][ny] = False
    return

dfs(0, 0)
