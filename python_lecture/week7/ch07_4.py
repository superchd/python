while True:
    how_many = int(input('Input count: '))
    
    information = []

    for i in range(how_many):
        example = input('Input student info (name, age, course list): ').split(', ')
        example.append(len(example) - 2)
        information.append(example)

    print('Input print options\n\
                1: By name\n\
                2: By age\n\
                3: By Courses count\n\
                9: Restart Program')
    temp = information

    while True:
        information = temp
        option = int(input('Enter the option: '))

        if option == 1:
            ans = sorted(information, key = lambda tu: tu[0])
        elif option == 2:
            ans = sorted(information, key = lambda tu: tu[1])
        elif option == 3:
            ans = sorted(information, key = lambda tu: tu[-1])
            # len courses 로 하면 간단함 .....
        elif option == 9:
            break
        
        for i in range(how_many):
            print('Student ', i + 1, ': (name: ',ans[i][0], ', age: ', ans[i][1], ', course list: [', sep = '', end = '')
            for j in range(2, len(ans[i]) - 1):
                if j != len(ans[i]) - 2:
                    print('\'',ans[i][j],'\'', sep = '', end = ', ')
                else:
                    print('\'', ans[i][j], '\'', sep = '', end = ']')
            print(')')


     
        

