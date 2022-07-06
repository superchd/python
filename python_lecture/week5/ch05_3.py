usage = int(input("Input usage:"))

if usage >= 0 and usage <= 100:
    print(usage, '*80 =', usage * 80)

elif usage > 100 and usage <= 200:
    print("100*80 +", usage - 100,"*120 =", 8000 + (usage - 100) * 120)

elif usage > 200:
    print("100*80 + 100*120 +", usage - 200, "*250 =", 8000 + 12000 + (usage - 200) * 250 )


