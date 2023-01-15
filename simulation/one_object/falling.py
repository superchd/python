import copy

n, m, k = map(int, input().split())

a = [
    list(map(int, input().split()))
    for _ in range(n)
]

sample = copy.deepcopy(a)

def check_raw(raw, m, k):
    for j in range(k - 1, m + k - 1):
        if a[raw][j] != 0:
            return False
    return True

def paint_raw(raw, m , k):
    for j in range(k - 1, m + k - 1):
        a[raw][j] = 1
    return

for r in range(n):
    if check_raw(r, m, k) == True:
        a = copy.deepcopy(sample)
        paint_raw(r, m, k)


for i in range(n):
    for j in range(n):
        print(a[i][j], end = ' ')
    print()


