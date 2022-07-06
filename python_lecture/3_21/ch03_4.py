import datetime
from datetime import datetime, timedelta

h = int(input("Input hours:"))
m = int(input("Input minutes:"))
seconds = int(input("Input seconds:"))
elapsed_seconds = int(input("Input elapsed seconds:"))

h = h * 3600
m = m * 60

s = h + m + seconds + elapsed_seconds;

hours = s // 3600
s = s - hours*3600
mu = s // 60
ss = s - mu*60
print(hours, ':', mu, ':', ss)

h = int(input("Input hours:"))
m = int(input("Input minutes:"))
seconds = int(input("Input seconds:"))
elapsed_seconds = int(input("Input elapsed seconds:"))

h = h * 3600
m = m * 60

s = h + m + seconds + elapsed_seconds;

hours = s // 3600
s = s - hours*3600
mu = s // 60
ss = s - mu*60
print(hours, ':', mu, ':', ss)

h = int(input("Input hours:"))
m = int(input("Input minutes:"))
seconds = int(input("Input seconds:"))
elapsed_seconds = int(input("Input elapsed seconds:"))

h = h * 3600
m = m * 60

s = h + m + seconds + elapsed_seconds;

hours = s // 3600
s = s - hours*3600
mu = s // 60
ss = s - mu*60
print(hours, ':', mu, ':', ss)

