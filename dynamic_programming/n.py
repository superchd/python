from re import X


def combination(first, second):
    ans = set()
    for f in first:
        for s in second:
            ans.add(f * s)
            ans.add(f / s)
            ans.add(f + s)
            ans.add(f - s)
    return ans

def update(all_number, ex, sum):
    for x in ex:
X        if all_number.get(x, None) == None:
            all_number[x] = sum
        elif all_number.get(x) > sum:
            all_number[x] = sum
    return all_number

def solution(N, number):
    answer = 0
    # setting
    table = []
    all_number = {}
    table.append(set())
    table.append(set([N]))
    
    for sum in range(2, 8):
        ex = []
        for i in range(1, sum):
            ex.append(combination(table[i], table[sum - i]))
        table.append(ex)
        all_number = update(all_number, ex, sum)
    
    if all_number.get(number) == None:
        return -1
    else :
        return all_number.get(number)

solution(5, 12)

