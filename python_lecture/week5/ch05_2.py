var1, var2, var3, var4 = map(int, input("Input heights: ").split())

first = var1
if first > var2:
    first = var2
if first > var3:
    first = var3
if first > var4:
    first = var4

if first == var1:
    second = var2
    if second > var3:
        second = var3
    if second > var4:
        second = var4
elif first == var2:
    second = var1
    if second > var3:
        second = var3
    if second > var4:
        second = var4
elif first == var3:
    second = var1
    if second > var2:
        second = var2
    if second > var4:
        second = var4
elif first == var4:
    second = var1
    if second > var2:
        second = var2
    if second > var3:
        second = var3

if first == var1 and second == var2:
    third = var3
    if third > var4:
        third = var4
        print("A, B, D, C")
elif first == var1 and second == var3:
    third = var2
    if third > var4:
        third = var4
        print("A, C, D, B")
elif first == var1 and second == var4:
    third = var1
    if third > var3:
        third = var3
        print("A, D, C, B")
elif first == var2 and second == var3:
    third = var1
    if third > var4:
        third = var4
        print("B, C, D, A")
elif first == var2 and second == var4:
    third = var1
    if third > var3:
        third = var3
        print("B, D, C, A")
elif first == var3 and second == var4:
    third = var1
    if third > var2:
        third = var2
        print("C, D, B, A")
if first == var2 and second == var1:
    third = var3
    if third > var4:
        third = var4
        print("B, A, D, C")
elif first == var3 and second == var1:
    third = var2
    if third > var4:
        third = var4
        print("C, A, D, B")
elif first == var4 and second == var1:
    third = var1
    if third > var3:
        third = var3
        print("D, A, C, B")
elif first == var3 and second == var2:
    third = var1
    if third > var4:
        third = var4
        print("C, B, D, A")
elif first == var4 and second == var2:
    third = var1
    if third > var3:
        third = var3
        print("D, B, C, A")
elif first == var4 and second == var3:
    third = var1
    if third > var2:
        third = var2
        print("D, C, A, B")





    






