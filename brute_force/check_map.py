n, m = map(int, input().split())

# 범위 밖인지 확인
def in_range(x, y, n, m):
    if 0 <= x < n and 0 <= y < m: return True
    else: return False

# dx, dy테크닉
dx = [i for i in range(1, n)]
dy = [j for j in range(1, n)]
nx, ny = 0, 0

# 그래프 그리기
graph = []
for _ in range(n):
    graph.append(list(map(str, input().split())))

answer = 0
path = []

# 시뮬레이션
for p in range(1, n):
    for q in range(1, m): 
        tx, ty = nx, ny
        nx, ny = nx + p, ny + q
        if in_range(nx, ny, n, m) and graph[nx][ny] != graph[tx][ty] and cnt <= 3:
            #print(f'nx = {nx}, ny = {ny}')
            cnt += 1
            path.append([nx, ny])
            pass
if len(path) == 2:
    print(path)
    answer += 1
print(answer)
