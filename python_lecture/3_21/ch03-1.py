def multiply(x, y):
    return x * y


num1 = int(input("Input number1:"))
num2 = int(input("Input number2:"))

a = []
for i in str(num2):
    a.append(i)


print(num1 * int(a[3]))
print(num1 * int(a[2]))
print(num1 * int(a[1]))
print(num1 * int(a[0]))

print(multiply(num1,num2))
