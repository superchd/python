n, m = tuple(map(int, input().split()))

def print_num(arr):
    for i in arr:
        print(i, end = " ")
    print()

def comb(cur_idx, arr):
    if cur_idx == m - 1:
        print_num(arr)
        return
# 아 인덱스 에러 뜬다 ...
    for i in range(1, n + 1):
        if i > arr[-1]:
            arr.append(i)
            perm(cur_idx + 1, arr)
            arr.pop()

comb(0, [])
