a, b, c= map(int, input("Input length of sides:").split())

maxi = a
if maxi <= b:
    maxi = b
if maxi <= c:
    maxi = c

sumi = a + b + c
if sumi - maxi > maxi :
    if a == b and b == c:
        print("Equilateral Triangle")
    else :    
        if a == b or b == c:
            print("Isosceles Triangle")
        elif a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2:
            print("Right-angled Triangle")
        else :
            print("Triangle")

else:
    print("Not Triangle")



