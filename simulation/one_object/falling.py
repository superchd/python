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

cnt = 0

if n == 1:
    print(1)
else :
    for r in range(n - 1):
        if next_line_blocked(r, m, k) == True:
            print(f"Okay, next line({r + 1}) is blocked!")
            a = copy.deepcopy(sample)
            paint_raw(r, m, k)
            cnt += 1
            break
    
    if cnt == 0:
        if next_line_blocked(n - 2, m ,k) == False:
            paint_raw(n - 1, m ,k)
        

    for i in range(n):
        for j in range(n):
            print(a[i][j], end = ' ')
        print()
