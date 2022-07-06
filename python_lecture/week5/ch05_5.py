a, b, c= map(int, input("Input angles: ").split())

if a + b + c == 180:
    if (a == 45 and b == 45) or (a == 45 or c == 45) or (b == 45 or c == 45):
        print("Rightangled Isosceles Triangle")
    else :    
        if a == b and b == c:
            print("Equilateral Triangle")
        elif a == b or b == c or c == a:
            print("Isosceles Triangle")
        elif a + b == c or a + c == b or b + c == a:
                print("Right-angled Triangle")
        else:
            print("Triangle")
else:
    print("Error")



