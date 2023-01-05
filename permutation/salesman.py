import copy

n = int(input())

a = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [0 for _ in range(n + 1)]

perm_lst = []

def perm(cur_idx, selected, visited):

    if cur_idx == n:
        element = copy.deepcopy(selected)
        perm_lst.append(element)
        visited = [0 for _ in range(n + 1)]
        return

    for i in range(1, n + 1):
        if visited[i]:
            continue
        
        selected.append(i)
        visited[i] = True
        perm(cur_idx + 1, selected, visited)
        visited[i] = False
        selected.pop(-1)            
    
perm(0, [], visited)


def count(ele):
    ele.append(ele[0])
    cnt = 0
    for i in range(n):
        cnt += a[ele[i] - 1][ele[i + 1] - 1]
    return cnt

s = []
for j in range(len(perm_lst)):
    s.append(count(perm_lst[j]))

print(min(s))
