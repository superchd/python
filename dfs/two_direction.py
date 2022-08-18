# input and draw grid
n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

visited = [[0] * m for _ in range(n)]

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
    nx , ny = x, y
    for i in range(2):
        # 여기가 고친 부분
    for i in range(2):
        nx, ny = x + dx[i], y + dy[i]
        if can_go(nx, ny) and not visited[nx][ny]:
            
            visited[nx][ny] = 1
            dfs(nx, ny)
        
    return


visited[0][0]= 1

dfs(0, 0)

print(visited[n-1][m-1])
