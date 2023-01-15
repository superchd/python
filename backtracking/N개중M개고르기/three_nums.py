import copy
import sys
n = int(input())

a = [
    input()
    for _ in range(n)
]

cand = []
comb = []

def end_test():
    if n < 3:
        return -1
    else:
        return 1

def find_num():
    for i in range(n):
        for j in range(n):
            if ('0' <= a[i][j] <= '9'):
                cand.append(a[i][j])
    return

def perm(cur_idx, cnt, current):

    global comb
    
    if cur_idx == len(cand):
        if cnt == 3:
            ex = copy.deepcopy(current)
            comb.append(ex)
        return 
    #print(f'cur_idx = {cur_idx}, cnt = {cnt}')
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
#print(comb)
mini = sys.maxsize
for c in comb:
    if mini > find_loc(c):
        mini = find_loc(c)
    #    mini = count_val(c)
if n < 3:
    print(-1)
else :
    print(mini)
