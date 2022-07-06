a = int(input("Input team A scores:"))
b = int(input("Input team B scores:"))

s1 = a % 10 
a      = a // 10

s1 += a % 10 
a      = a // 10

s1 += a % 10 
a      = a // 10

s1 += a % 10 
a      = a // 10

s1 += a % 10 
a      = a // 10

s1 += a % 10 
a      = a // 10


s2 = b % 10 
b      = b // 10

s2 += b % 10 
b      = b // 10

s2 += b % 10 
b      = b // 10

s2 += b % 10 
b      = b // 10

s2 += b % 10 
b      = b // 10

s2 += b % 10 
b      = b // 10

print(s1 > s2)
