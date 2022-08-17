n, m = map(int, input().split())

# 범위 밖인지 확인
def in_range(x, y, n, m):
    if 0 <= x < n and 0 <= y < m: return True
    else: return False

nx, ny = 0, 0

# 그래프 그리기
graph = []
for _ in range(n):
    graph.append(list(map(str, input().split())))

cnt = 0
path = []

for i in range(1, n):
    for j in range(1, m):
        for k in range(i + 1, n):
            for l in range(j + 1, m):
                nx, ny = nx + k, ny + l
                if in_range(nx, ny, n, m) and graph[nx][ny] != graph[i][j]:
                    cnt += 1
print(cnt)
