# 변수 선언 및 입력
k, n = tuple(map(int, input().split()))
selected_nums = []

# print num
def print_num(arr):
    for i in arr:
        print(i, end = " ")
    print()

# perm 
def perm(cur_idx, arr):

    if cur_idx == n:
        print_num(arr)
        return 

    for i in range(1, k + 1):
        arr.append(i)
        perm(cur_idx + 1, arr)
        arr.pop()
    
perm(0, [])


        




