matrix = [] 

def my_input(n, m):
    global matrix
    for i in range(n):
        num = input()
        ex = []
        for j in range(m):
            k = int(num[j])
            row = []
            row.append(k)
            row.append(i)
            row.append(j)
            ex.append(row)
        matrix.append(ex)
    return

def make_square(target, i, j, n, m):
    answer = []
    max = n
    if max > m:
        max = m
    condition = True
    my_num = []
    for k in range(max):
        if i + k < n and j + k < m:
            if target == matrix[i + k][j][0] and target == matrix[i][j + k][0] and target == matrix[i + k][j + k][0]:
                answer.append(k + 1)
    
    if len(answer) == 0:
        return 100000
    else :
        answer.sort(reverse = True)
    return answer[0]

def my_sol(n, m):
    my_list = []
    global matrix
    for i in range(n):
        for j in range(m):
            target = matrix[i][j][0]
            my_list.append(make_square(target, i, j, n , m))
    my_list.sort(reverse = True)
    if len(my_list) == 0:
        return 'error'
    else :
        print(pow(my_list[0],2))
    return


def main():
    n , m = input().split(' ')
    n = int(n)
    m = int(m)
    my_input(n, m)
    my_sol(n ,m)

if __name__ == "__main__":
	main()       