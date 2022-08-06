


from symbol import pass_stmt


def my_input():

    N = int(input())
    lst = []
    for i in range(N):
        s, e = map(int, input().split())
        ex = []
        ex.append(s)
        ex.append(e)
        lst.append(ex)
    
    return lst


def solution(lst):
    flag = 0
    cnt = 0
    for l in lst:
        if flag == 0:
            s = l[0]
            e = l[1]
            cnt += 1
            flag = 1
        else :
            if l[0] >= e and l[1] > e:
                s = l[0]
                e = l[1]
                cnt += 1 
    print(cnt)

lst = my_input()
solution(lst)