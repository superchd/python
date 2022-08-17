def beautiful(k, n, ans):

    # end condition
    if k == n:
        return ans

    for i in range(1, 5):
        if i == 1: beautiful(k + i, n, 2 * ans)
        elif i == 2: 

n = int(input())

beautiful(1, n, 1)
