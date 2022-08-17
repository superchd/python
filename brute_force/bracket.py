 inp = input()

cnt = 0

for i in range(len(inp)):
    if inp[i] == '(':
        for j in range(i, len(inp)):
            if inp[j] == ')':
                cnt += 1

print(cnt)



