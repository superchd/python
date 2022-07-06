import datetime

from datetime import datetime, timedelta
def multiply(x, y):
    return x * y

def hms():
    global s
    hours = s // 3600
    s = s - hours*3600
    mu = s // 60
    ss = s - mu*60
    print(hours, ':', mu, ':', ss)

t1_h = int(input("Input hours for t1:"))
t1_m = int(input("Input minutes for t1:"))
t1_s = int(input("Input seconds for t1:"))
t2_h = int(input("Input hours for t2:"))
t2_m = int(input("Input minutes for t2:"))
t2_s = int(input("Input seconds for t2:"))

t1_h = t1_h * 3600
t1_m = t1_m * 60
t2_h = t2_h * 3600
t2_m = t2_m * 60


s = t1_h + t1_m + t1_s + t2_h + t2_m + t2_s

hms()
