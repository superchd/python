inp = input()

nx, ny = 0, 0 
dir_num = 3
# 시계방향
dx = [1, 0, -1, 0]
dy = [0, -1, 0 ,1]
turn_L = [3, 0, 1, 2]
turn_R = [1, 2, 3, 0]

for i in range(len(inp)):

    #rotation direction
    if inp[i] == 'L'      : dir_num = turn_L[dir_num]
    elif inp[i] == 'R'    : dir_num = turn_R[dir_num]
    else :
        nx, ny = nx + dx[dir_num], ny + dy[dir_num]
print(nx, ny)
 
'''
시계방향
[0, 1, 2, 3] -> [1, 2, 3, 0]
반시계방향
[0, 1, 2, 3] -> [3, 0, 1, 2]
'''

