import datetime

def process_data(booked, unbooked):
    new_booked = []
    new_unbooked = []

    for b in booked:
        ex = []
        h, m = b[0].split(sep = ':')
        d = datetime.datetime(2022, 7, 17, int(h), int(m))
        ex.append(d)
        ex.append(b[1])
        ex.append("booked")
        new_booked.append(ex)

    for u in unbooked:
        ex = []
        h, m = u[0].split(sep = ':')
        d = datetime.datetime(2022, 7, 17, int(h), int(m))
        ex.append(d)
        ex.append(u[1])
        ex.append("unbooked")
        new_unbooked.append(ex)
    
    return new_booked, new_unbooked

def candidate(idx, customer):

    can = []
    for i in range(idx + 1, len(customer)):
        if (customer[i][0] - customer[idx][0]).seconds <= 600:
            can.append(customer[i])
        
        else : break
            
    return can

def selection(can):
    flag = 0
    
    for c in can:
        if c[2] == "booked":
            flag = 1
            return c
    
    return can

def solution(booked, unbooked):
    answer = []

    booked , unbooked = process_data(booked, unbooked)
    customer = booked + unbooked

    customer.sort(key=lambda x : x[0])
   
    while len(customer) != 0:
        answer.append(customer[0][1])
        can = candidate(0, customer)
        if len(customer) == 1 : 
            customer.remove(customer[0])
            break

        if len(can) >= 1: s = selection(can)
            
        else            : s = customer[1]

        answer.append(s[1])
        customer.remove(customer[0])
        customer.remove(s)

    print(answer)
    return answer


booked = [["09:10", "lee"]]
unbooked = [["09:00", "kim"], ["09:05", "bae"]]
solution(booked, unbooked)