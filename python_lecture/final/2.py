matrix = [] 

def my_input(n, m):
    global matrix
    for i in range(n):
        num = input().split(' ')
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

def my_sol(n, m):
    my_list = []
    global matrix

    max_num = n - 1 + m 
    for k in range(max_num):
        for i in range(n):
            for j in range(m):
                if matrix[i][j][1] + matrix[i][j][2] == k:
                    print(matrix[i][j][0], end = ' ')
        print()
  


def main():
    n , m = input().split(' ')

    n = int(n)
    m = int(m)
    my_input(n, m)
    my_sol(n ,m)

if __name__ == "__main__":
	main()       