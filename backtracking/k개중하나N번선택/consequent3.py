k, n = tuple(map(int, input().split()))

def print_num(arr):
    for i in arr:
        print(i, end = " ")
    print()

# 인덱스가 배열의 값을 참조못하는 인덱스일까봐 걱정이네 , 그냥 간단하게 조건을 거네



def perm(cur_idx, arr):
    if cur_idx == n:
        print_num(arr)
        return

    for i in range(1, k + 1):
        if cur_idx >= 2 and i == arr[-1] \
                        and i == arr[-2]:
            continue
        
        else:
            arr.append(i)
            perm(cur_idx + 1, arr)
            arr.pop()
    
perm(0, [])
            

