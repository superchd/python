# prime_list는 1부터 10000사이의 소수가 오름차순으로 저장된 리스트예요.
from prime import prime_list
import math

def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False 
    return True

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > target:
            high = mid - 1
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
    return low
 
# 합계가 짝수가 되는 두 소수를 찾는 함수예요.
def goldbach(arr):
    # 합계가 짝수가 되는 두 소수를 작은 수부터 차례로 리스트에 저장해 주세요.
    for a in arr:
        num_list = []
        for p in prime_list:
            if a > p: num_list.append(p)
            else : break
        l = len(num_list)
        first_list = num_list[:int(l / 2)]
        second_list = num_list[int(l / 2):]
        #print(first_list, second_list) 

        comb = []
        if a % 2 == 0 and is_prime(a / 2) == True:
            comb.append([a / 2, a / 2])
        for f in first_list:
            for s in second_list:
                if f + s == a:
                    comb.append([f, s])
        
        print(comb)


    return None

arr = [int(x) for x in input().split()]

for i in goldbach(arr):
    print(i[0], i[1])