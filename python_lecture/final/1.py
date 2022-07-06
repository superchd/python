class student :
    c = 0
    p = 0
    rank = 0

    def __init__(self, c, p):
        self.c = c
        self.p = p
                
    

def flag(tc, c):
    win = 0
    sum_a = 0
    sum_b = 0

    if tc.c > c.c:
        win += 1
    elif tc.c < c.c:
        win -= 1
    
    if tc.p > c.p:
        win += 1
    elif tc.p < c.p:
        win -= 1

    sum_a = tc.c + tc.p
    sum_b = c.c + c.p

    if win > 0 :
        return 1
    elif win < 0:
        return -1
        
    if sum_a > sum_b:
        return 1
    elif sum_a < sum_b:
        return -1
    else : return 0
    

students = []

#cnt, targetId = map(int, input().split())

cnt = input()
cnt = int(cnt)

for i in range(cnt):
    c, p = map(int, input().split())
    students.append(student(c, p))

ranks = []
# 동점자 처리가 좀 어렵네 !! 

for tc in students:
    rank = 1
    for c in students:
        if tc != c:
            if flag(tc, c) == -1: rank += 1
    ranks.append(rank)

for r in ranks:
    print(r, end = ' ')

