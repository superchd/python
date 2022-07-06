while True:
    floor = int(input('input height:'))
    # 4층 출력
    for x in range(floor, 0, -1):
        print(x, end = ' ')
        # 공백 출력
        for y in range(0, floor - x, 1):
            print(' ', end = '')
        # print *
        for z in range(x - 1, 0, -1):
            print('*', end = '')
        # print floor
        print(x, end = '')
        # print *
        for z in range(x - 1, 0, -1):
            print('*', end = '')
        print('\n')




    # 3층 출력
    # 2층 출력
    # 1층 출력


