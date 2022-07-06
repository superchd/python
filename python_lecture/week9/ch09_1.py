how_many = int(input())

Strs = []
answer = []

for i in range(how_many):
    inpStr = input()
    Strs.append(inpStr)

for j in range(len(inpStr)):
    diff = True
    for i in range(how_many - 1):
        if Strs[i][j] != Strs[i + 1][j]:
            diff = False
    if diff == True:
        answer.append(Strs[i][j])
    else :
        answer.append('?')

for i in range(len(answer)):
    print(answer[i],end = '')


    