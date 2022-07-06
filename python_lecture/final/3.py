def gcd(a, b):
    while a % b != 0:
        mod = a % b
        a = b
        b = mod
    return b

class fraction :
    n = 0
    d = 0 
    value = int(0)

    def __init__(self, n, d):
        self.n = n
        self.d = d
        self.value = n / d
      
    def __add__(self,other):
        a, b = self.n, self.d
        c, d = other.n, other.d

        g1 = gcd(b, d)
        final_d = b * d // g1
        final_n = a * (d//g1) + c * (b//g1)

        g2 = gcd(final_d, final_n)
        ans = ''
        ans += str(final_n//g2) + '/' + str(final_d//g2) 
        
        return ans

    def __lt__(self,other):
        return self.value < other.value 

    def __str__(self):
        ans = ''
        ans += str(self.n) + '/' + str(self.d)
        return ans



cnt, a, b = map(int, input().split())
fractions = []
for i in range(cnt):
    n, d = map(int, input().split())
    f = fraction(n, d) # n:numerator, d:denominator
    fractions.append(f)
print(fractions[a] + fractions[b])
fractions.sort()
print(*fractions)

