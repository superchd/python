def alphabetToNumber(s):
    if s.isdigit(): return int(s)
    elif s in ['A','B','C']:return 2
    elif s in ['D','E','F']:return 3
    elif s in ['G','H','I']:return 4
    elif s in ['J','K','L']:return 5
    elif s in ['M','N','O']:return 6
    elif s in ['P','Q','R','S']:return 7


while True:
    inpStr = input('Input: ')
    inpNumStr = inpStr.split('-')
    lens = list(map(len, inpNumStr))
    if lens != [1, 3, 4, 3] and lens != [1, 3, 3, 4]:
        print('input error')
        continue
    
    numList = [y for x in inpNumStr for y in x]
    #numList = list(inpStr.replace('-',' '))
    
    sum = 0
    for i in numList:
        sum += alphabetToNumber(i)
    print(sum) 
