n = int(input())

a = [ 
    list(map(int, input().split()))
    for _ in range(2 * n)
]

dp = [0 for _ in range(2 * n)]


dp[1] = max(a[0][0] + a[1][1], a[0][1] + a[1][0])
#print(a)

for i in range(3, 2 * n, 2):
    box = max(a[i - 1][0] + a[i][1], a[i - 1][1] + a[i][0])
    dp[i] = dp[i - 2] + box

print(dp)
print(dp[2 * n - 1])

    
