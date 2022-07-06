import datetime

datestr, timestr, n = input().split()
year, month, day = datestr.split('-')
hour, minute, second = timestr.split(':')

current = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))

for i in range(int(n)):
    add = input()
    for j in range(len(add)):
        if add[j].isalpha():
            flag = add[j]
        cnt = j
    if add[0] == '-':
        sign = -1
    else: sign = 1
    add = float(add[1:cnt])
    add = sign * add

    if flag == 'd':
        current = current + datetime.timedelta(days = add)
    elif flag == 'h':
        current = current + datetime.timedelta(hours = add)
    elif flag == 'M':
        current = current + datetime.timedelta(minutes = add)
    elif flag == 's':
        current = current + datetime.timedelta(seconds = add)
    print(current.strftime("%Y/%m/%d %H-%M-%S"))
    

