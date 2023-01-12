import copy
import sys
n = int(input())

a = [
    input()
    for _ in range(n)
]

cand = []
comb = []

def find_num():

    for i in range(n):
        for j in range(n):
            if ('0' <= a[i][j] <= '9'):
                cand.append(a[i][j])
    return

def perm(cur_idx, cnt, current):

    global comb
    #print(f'cur_num = {cur_num}, cnt = {cnt}')
    if cur_idx == n + 1:
        if cnt == 3:
            ex = copy.deepcopy(current)
            comb.append(ex)
        return 

    current.append(cand[cur_idx])
    perm(cur_idx + 1, cnt + 1, current)
    current.pop()
    perm(cur_idx + 1, cnt, current)

def find_loc(nums):
    start = []
    dic = {}
    end = []
    for i in range(n):
        for j in range(n):
            if a[i][j] == 'S':
                start.append((i, j))
            elif a[i][j] == 'E':
                end.append((i, j))
            elif a[i][j] in nums:
                dic[a[i][j]] = (i, j)
    
    dic = sorted(dic.values(), reverse=True)
    mid = []
    mid.append(start[0])
    for d in dic:
        mid.append(d)
    mid.append(end[0])
    cnt = 0
    for i in range(len(mid) - 1):
        dx = dist(mid[i + 1], mid[i])
        cnt += dx
        
    #print(cnt)    
    return cnt 

def dist(a, b):
    ax, ay = a[0], a[1]
    bx, by = b[0], b[1]
    return abs(ax - bx) + abs(ay - by)
    
find_num()
cand.sort()
perm(0, 0, [])
mini = sys.maxsize
for c in comb:
    if mini > find_loc(c):
        mini = find_loc(c)
    #    mini = count_val(c)
print(mini)
