print("## Please enter the information to send the two items. ##")

Recipient = input("Recipient: ")
Address = input("Address: ")
Item_1 = int(input("Weight(g) of Item #1: "))
Item_2 = int(input("Weight(g) of Item #2: "))
print("-----------------------------")

print("** TO ==> ", Recipient)
print("** Address ==> ", Address)
print("** Total shipping cost ==> $",(Item_1 + Item_2) / 2) 
