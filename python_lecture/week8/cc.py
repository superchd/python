import datetime

def input_date():

    y, m, d = input("Input date: ").split('-')
    y = int(y)
    m = int(m)
    d = int(d)

    return y, m, d

def is_leap(num):
    if (num % 4) ==0:
        if (num % 400) == 0: 
            return True
        elif (num % 100) == 0: 
            return False
        else: 
            return True
    else: 
        return False

def get_day_name(year, month, day):
    dt = datetime.datetime(year, month, day)
    dt = int(dt.strftime("%j"))
    count_day = 0
    for i in range(year):
        if is_leap(i): 
            count_day += 366
        else: 
            count_day += 365
    count = (count_day + dt - 366) %  7 

    return {0: '일요일', 1: "월요일", 2: "화요일", 3: "수요일",\
            4: "목요일", 5: "금요일", 6: "토요일"}[count]

if __name__ == "__main__":
    year, month, day = input_date()
    day_name = get_day_name(year, month, day)
    print(day_name)
