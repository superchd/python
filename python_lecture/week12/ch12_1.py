
class num :
    number = 0
    rm = 0

    def __init__(self, number):
        self.number = number
        self.rm = number % 3

    def printnum(self) :
        print(self.number, end = ' ')


def bubbleSort(nums):
    n = len(nums)
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j].number > nums[j + 1].number:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    
    return nums


def specialSort(x):

    for i in range(len(x) - 1):
        for j in range(len(x) - i - 1):
            if x[j].rm < x[j + 1].rm:
                x[j], x[j + 1] = x[j + 1], x[j]
    

nums = []

my_input = list(map(int, input().split()))

for i in range(len(my_input)):
    nums.append(num(my_input[i]))

bubbleSort(nums)
for c in nums: c.printnum()
print()
specialSort(nums)
for c in nums: c.printnum()

#specialSort(bs_array)
