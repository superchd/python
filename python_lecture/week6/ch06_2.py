while True:
    a, b= map(int, input("Input two numbers:").split())
    if a > b:
        temp = a
        a = b
        b = temp
    for x in range(a + 1, b):
        flag = 0
        for y in range(2, x):
            if (x % y == 0):
                flag = 1

        if (flag == 0):
            if (x != b) and (x != b-1):
                print(x, end = ',')
            else:
                print(x)



