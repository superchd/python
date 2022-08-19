n, t = map(int, input().split())

a = [
    list(map(int, input().split()))
    for _ in range(2)
]

for _ in range(t):
    # 첫줄 컨베이어 이동
    # 1. 1번째 줄에서 2번째 줄로 내려갈 원소 정하기 
    down = a[0][n - 1]
    # 2. 2번째 줄에서 1번째 줄로 올라갈 원소 정하기
    up = a[1][-1]

    # 3. 1번째 줄 원소 slide
    a[0] = [up] + a[0][0:-1]

    # 4. 2번째 줄 원소 slide
    a[1] = [down] + a[1][0 : n - 1]

for i in range(2):
    print(*a[i])




