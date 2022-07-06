class car :
    id = 0
    price = 0 
    year = 0 
    km = 0

    def __init__(self, id, price, year, km):
        self.id = id
        self.price = price
        self.year = year
        self.km = km
        print(id, "added")

    def __lt__(self,other):
        return self.price < other.price

    def printInfo(self) :
        print(f'id={self.id} | price={self.price} | year={self.year} | km={self.km}')

#define class here
# do not modify codes below
cars = []
cnt = int(input())

for i in range(cnt):
    id, price, year, km = map(int, input().split())
    cars.append(car(id, price, year, km))

cars.sort(reverse=True)

for c in cars: c.printInfo()

