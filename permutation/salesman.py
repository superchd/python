n = int(input())

a = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [0 for _ in range(n + 1)]

perm_lst = []

def perm(cur_idx, selected, visited):

    if cur_idx == n:
        perm_lst.append(selected)
        visited = [0 for _ in range(n + 1)]
        print(selected)
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
print(perm_lst)
