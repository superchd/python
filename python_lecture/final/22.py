
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

def main():
    n , m = input().split(' ')
    n = int(n)
    m = int(m)
    my_input(n, m)
   # my_sol(n ,m)

if __name__ == "__main__":
	main()       