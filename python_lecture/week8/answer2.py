md = [0,31,28,31,30,31,30,31,31,30,31,30,31]
dow = ['MON','TUE','WED','THU','FRI','SAT','SUN']

def isLeapYear(y):
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)

def getMonthDays(y, m):
    if isLeapYear(y) and m == 2 : return 29
    else: return md[m]

while True:
    year, month, day = map(int, input('input: ').split('-'))
    if year < 1 or year > 9999 or month < 1 or month > 12 or day < 1 or day > getMonthDays(year, month):
        print('input error')
        continue
    
    totalDays = 0
    for i in range(1, year):
        totalDays += 366 if isLearYear(y) else 365
    for m in range(1, month):
        totalDays += getMonthDays(year, m)
    totalDays += day 
    # calc total Days
    print(dow[totalDays % 7])