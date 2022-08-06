import time


table = []

def make_table(n, lost, reserve):
    global table

    for i in range(n):
        table.append(1)

    for i in range(len(lost)):
        table[lost[i]] = 0

    for i in range(len(reserve)):
        table[reserve[i] - 1] += 1

def solution(n, lost, reserve):

    global table


##  전역변수 table을 정의
    make_table(n, lost, reserve)

##  예외처리 (인덱스 0일때)
    if table[0] == 0:
        if table[1] == 2:
            table[1] == 1
            table[0] == 1

##  보통의 경우 처리
    for i in range(1, len(table) - 1):
        if table[i] == 0:
            if table[i - 1] == 2 and table[i + 1] != 2:
                table[i - 1] = 1
                table[i]     = 1

            elif table[i - 1] != 2 and table[i + 1] == 2:
                table[i + 1] = 1
                table[i]     = 1

            elif table[i - 1] == 2 and table[i + 1] == 2:
                table[i - 1] = 1
                table[i]     = 1

    if table[len(table) - 1] == 0:
        if table[len(table) - 2] == 2:
            table[len(table) - 2] = 1
            table[len(table) - 1] = 1

    cnt = 0

    for t in table:
        if t >= 1: cnt += 1

    return cnt
