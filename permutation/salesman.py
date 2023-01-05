import copy
import sys

n = int(input())
val = sys.maxsize

a = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [0 for _ in range(n + 1)]

perm_lst = []

def perm(cur_idx, selected, visited):

    if cur_idx == n - 1:
        element = copy.deepcopy(selected)
        perm_lst.append(element)
        visited = [0 for _ in range(n + 1)]
        return

    for i in range(2, n + 1):
        if visited[i]:
            continue
        selected.append(i)
        visited[i] = True
        perm(cur_idx + 1, selected, visited)
        visited[i] = False
        selected.pop(-1)            
    
visited[0] = True
perm(0, [1], visited)

#print(perm_lst)

def count(ele):
    cnt = 0
    ele.append(1)
    for i in range(n):
        if a[ele[i] - 1][ele[i + 1] - 1] == 0:
            return -1
        cnt += a[ele[i] - 1][ele[i + 1] - 1]
    return cnt

s = []

for j in range(len(perm_lst)):
    if count(perm_lst[j]) != -1:
        if count(perm_lst[j]) < val:
            val = count(perm_lst[j])
print(val)
