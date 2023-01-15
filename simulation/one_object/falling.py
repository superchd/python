import copy

n, m, k = map(int, input().split())

a = [
    list(map(int, input().split()))
    for _ in range(n)
]

sample = copy.deepcopy(a)

def next_line_blocked(raw, m, k):
    for j in range(k - 1, m + k - 1):
        if a[raw + 1][j] != 0:
            #print(f'Okay Im in next_line_blocked and {j} is 1 so, it returns false')
            return True
    return False

def paint_raw(raw, m , k):
    for j in range(k - 1, m + k - 1):
        a[raw][j] = 1
    return


did = 0
for r in range(n - 1):
    if next_line_blocked(r, m, k) == True:
        #print(f"Okay, next line({r + 1}) is blocked!")
        a = copy.deepcopy(sample)
        paint_raw(r, m, k)
        did += 1
        break

## last line check


cnt = 0
for j in range(k - 1, m + k - 1):
    if a[n - 1][j] == 0:
        cnt = cnt + 1

if cnt == m and did == 0:
    paint_raw(n - 1, m , k)

for i in range(n):
    for j in range(n):
        print(a[i][j], end = ' ')
    print()
