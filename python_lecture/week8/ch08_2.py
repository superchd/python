month_days = [0,31,28,31,30,31,30,31,30,31,30,31,30]
error = 0

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

def input_error(y, m, d):
    if is_leap(y):
        month_days[2] = 29

    if month_days[m] < d or y == 0:
        return True
    else:
        return False

def input_date():
    y, m, d = input("Input date: ").split('-')
    y = int(y)
    m = int(m)
    d = int(d)
    return y, m, d

def get_day_name(year, month, day):

    if input_error(year, month, day) == True:
        return 'Input error'
    if is_leap(month):
        month_days[2] = 29
    else:
        total_days = 0
        for year_item in range(1, year):
            total_days = total_days + 365
            if is_leap(year_item):
                total_days = total_days + 1
            else:
                pass

        for month_index in range(1, month):
            total_days = total_days + month_days[month_index]

        total_days = total_days + day

        day_name = total_days % 7
        return {0: 'SUN', 1: "MON", 2: "TUE", 3: "WED",\
                4: "THU", 5: "FRI", 6: "SAT"}[day_name]

if __name__ == "__main__":
    year, month, day = input_date()
    day_name = get_day_name(year, month, day)
    print(day_name)