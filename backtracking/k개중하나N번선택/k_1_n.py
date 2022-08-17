def choose(cur, K, N):
    # 종료조건
    if len(cur) == N:
        print(*cur)
        return

    for i in range(1, K + 1):
        cur.append(i)
        choose(cur, K, N)
        cur.pop()
    
    return

K, N = map(int, input().split())

choose([], K, N)
