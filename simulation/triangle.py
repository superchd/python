n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

for _ in range(t):
    temp = l[n - 1]
    for i in range(n - 1, 0, -1):
        l[i] = l[i - 1]
    l[0] = d[n - 1]

    temp2 = r[n - 1]
    for i in range(n - 1, 0, -1):
        r[i] = r[i - 1]
    r[0] = temp


    for i in range(n - 1, 0, -1):
        d[i] = d[i - 1]
    d[0] = temp2

for e in l:
    print(e, end = ' ')
print()

for e in r:
    print(e, end = ' ')
print()

for e in d:
    print(e, end = ' ')
print()
