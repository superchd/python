def in_range(x, y, n):
    if x >= 0 and x <= n - 1 and y >= 0 and y <= n - 1:
        return True
    else :return False

# 그래프
graph = []

# 입력받기
n = int(input())
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 초기조건 설정
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# dx, dy 테크닉
nx, ny = 0, 0

# 완전 탐색
cnt = 0
for i in range(n):
    for j in range(n):
        flag = 0 
        for d in range(4):
            nx, ny = i + dx[d], j + dy[d]
            if in_range(nx, ny, n) and graph[nx][ny] == 1:
                flag += 1
        if flag >= 3:
            cnt += 1
print(cnt)
