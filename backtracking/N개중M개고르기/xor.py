import copy

ans = []

def combination(arr, nums, m):
    global ans
    if len(arr) == m:
        #print(*arr)
        val = 0
        for i in range(0, m):
            val ^= arr[i]
        #print(val)
        ans.append(val)
        return

    l = len(nums)

    for i in range(1, l):
        arr.append(nums[i])
        temp = copy.deepcopy(nums)
        del nums[i]
        combination(arr, nums, m)
        arr.pop()
        nums = temp

    return
    
n, m = map(int, input().split())
nums = list(map(int, input().split()))


combination([], nums, m)
print(ans)
print(max(ans))
