import sys

INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize

n = int(input())

home = list(map(int, input().split()))

min_val = INT_MAX

for i in range(len(home)):
    sum = 0
    for j in range(len(home)):
        if i != j:
            sum += abs(j - i) * home[j]
    if sum < min_val:
        min_val = sum
print(min_val)
            
