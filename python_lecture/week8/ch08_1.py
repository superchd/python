def flag(num):
    if num >= 'A' and num <= 'C':
        num = '2'
    elif num >= 'D' and num <= 'F':
        num = '3'
    elif num >= 'G' and num <= 'I':
        num = '4'
    elif num >= 'J' and num <= 'L':
        num = '5'
    elif num >= 'M' and num <= 'O':
        num = '6'
    elif num >= 'P' and num <= 'S':
        num = '7'
    elif num >= 'T' and num <= 'V':
        num = '8'
    elif num >= 'W' and num <= 'Z':
        num = '9'

    return int(num)

while True:
    example = input('Input telephone number: ').split('-')
    sum = 0
    alpha = 0
    digit = 0

    for i in range(len(example)):
        for j in range(len(example[i])):
            if example[i][j].isdigit():
                digit = 1
            elif example[i][j].isalpha():
                alpha = 1
            sum = sum + flag(example[i][j])
    if digit + alpha != 2:
        print('Input error')
    else :
        print(sum)



