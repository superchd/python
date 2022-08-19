import copy
# 입력받기
n = int(input())

arr = []
for _ in range(n):
    arr.append([int(input())])

remover = []
for _ in range(2):
    s, e = map(int, input().split())
    remover.append((s - 1, e - 1))

# initial condition
BLANK = 0

end_of_array = n

end_of_temp_array = 0

temp = [0] * n

s, e = remover[0]
end_of_temp_array = 0
for i in range(end_of_array):
    if not (s <= i <= e):
        temp[end_of_temp_array] = arr[i]
        end_of_temp_array += 1


arr = copy.deepcopy(temp)
s, e = remover[1]
end_of_temp_array = 0
end_of_array = len(temp)
temp2 = [0] * end_of_array

for i in range(end_of_array):
    if not (s <= i <= e):
        temp2[end_of_temp_array] = arr[i]
        end_of_temp_array += 1

#print(temp2)
answer = []
for t in temp2:
    if t != 0:
        answer.append(t)
    
print(len(answer))
for t in answer:
    print(*t)
