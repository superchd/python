import functools

# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
a = list(map(int, input().split()))

ans = []

def find_max_xor(curr_idx, cnt, curr_val):
    global ans

    if cnt == m:
        ans.append(curr_val)
        return

    if curr_idx == n:
        return

    #선택하는경우
    find_max_xor(curr_idx + 1, cnt + 1, curr_val ^ a[curr_idx])

    #선택하지 않는경우
    find_max_xor(curr_idx + 1, cnt, curr_val)
    return

find_max_xor(0, 0, 0)
print(max(ans))
