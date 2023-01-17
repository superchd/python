import copy
import sys
n = int(input())

a = [
    input()
    for _ in range(n)
]

cand = []
start = (-1, -1)
end = (-1, -1)

ans = sys.maxsize

def find_num():
    global cand
    for i in range(n):
        for j in range(n):
            if ('0' <= a[i][j] <= '9'):
                cand.append(a[i][j])
    return

# 시작포인트와 끝포인트 찾아보기
for i in range(n):
    for j in range(n):
        if a[i][j] == 'S':
            start = (i, j)
        elif a[i][j] == 'E':
            end = (i, j)
        
def dist(a, b):
    ax, ay = a[0], a[1]
    bx, by = b[0], b[1]
    dx = abs(ax - bx)
    dy = abs(ay - by)
    return dx + dy

def calculate_move(nums):
    points = []
    for i in range(n):
        for j in range(n):
            if a[i][j] in nums:
                points.append((i, j))
    
    move_sum = dist(start, points[0])
    for i in range(len(points) - 1):
        move_sum += dist(points[i], points[i + 1])
    move_sum += dist(points[-1], end)
    return move_sum

def find_min_move(cur_idx, cnt, nums):
    global ans
    if cur_idx == len(cand) - 1:
        if cnt == 3:
            if ans > calculate_move(nums):
                ans = calculate_move
        return

    # 현재 idx를 선택했을 때
    nums.append(cur_idx)
    find_min_move(cur_idx + 1, cnt + 1, nums)
    # 현재 idx를 선택하지 않고 넘어갈 때
    nums.pop()
    find_min_move(cur_idx + 1, cnt, nums)    

find_min_move(0, 0, [])
print(ans)
