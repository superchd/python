import datetime as dt
from datetime import time


def parseTime(inp):
    sstr, estr = inp.split()
    sh, sm, ss = map(int, sstr.split(':'))
    eh, em, es = map(int, estr.split(':'))
    return dt.datetime(1,1,1, sh, sm, ss), dt.datetime(1,1,1, eh, em, es)


cnt = int(input())
score = 0

s1, e1 = dt.datetime(1,1,1,0,0,0), dt.datetime(1,1,1,9,0,0)
s2, e2 = dt.datetime(1,1,1,9,0,0), dt.datetime(1,1,1,18,0,0)
s3, e3 = dt.datetime(1,1,1,18,0,0), dt.datetime(1,1,2,0,0,0)

for i in range(cnt):
    start, end = parseTime(input())

    z1s = min(e1, end) - max(s1, start)
    if z1s > dt.timedelta():
        score += z1s.seconds * 2

    z2s = min(e2, end) - max(s2, start)
    if z2s > dt.timedelta():
        score += z2s.seconds
    
    pen = min(start, e2) - s2
    if pen > dt.timedelta():
        score -= pen.seconds * 5

    if end > s2:
        s2 = end
    

    z3s = min(e3, end) - max(s3, start)
    if z3s > dt.timedelta():
        score += z3s.seconds * 2
print(score)











