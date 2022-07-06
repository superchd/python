while True:
    a, b= map(int, input("Input two numbers:").split())
    if a > b:
        temp = a
        a = b
        b = temp
    for x in range(a + 1, b):
        if (x % 2 == 1):
            if (x != b) and (x != b-1):
                print(x, end = ',')
            else:
                print(x)


