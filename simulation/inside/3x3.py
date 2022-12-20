# 변수 선언 및 입력
n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

num_max = 0

def get_gold_num(i, j):
    cnt = 0
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            if grid[x][y] == 1:
                cnt += 1
    return cnt

for i in range(n):
    for j in range(n):
        if i + 2 < n and j + 2 < n:
            num = get_gold_num(i, j)
            if num >= num_max:
                num_max = get_gold_num(i, j)

print(num_max)
