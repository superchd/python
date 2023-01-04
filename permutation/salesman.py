n = int(input())

a = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [0 for _ in range(n)]

perm_lst = []

def perm(cur_idx, selected, visited):

    if cur_idx == n - 1:
        perm_lst.append(selected)
        visited = [0 for _ in range(n)]
        return

    for i in range(n):
        if not visited[i]:
            selected.append(i)
            visited[i] = True
            perm(cur_idx + 1, selected, visited)
    
perm(0, [], visited)
print(perm_lst)
