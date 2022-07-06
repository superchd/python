word = input("Input strings of length 5:")

a = word[0] + word[0] + word[0]
a = a + word[1] + word[1] + word[1]
a = a + word[2] + word[2] + word[2]
a = a + word[3] + word[3] + word[3]
a = a + word[4] + word[4] + word[4]
c = a
a = a + c
a = a + c
a = a + c
a = a + c
print(a)
