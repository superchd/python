def combination(arr, N, M):

    if len(arr) == M:
        print(*arr)
        return

    for i in range(max(arr) + 1, N + 1):
        arr.append(i)
        combination(arr, N, M)
        arr.pop()
    
    return

N, M = map(int, input().split())
for k in range(1, N - M + 2):
    combination([k], N, M)
