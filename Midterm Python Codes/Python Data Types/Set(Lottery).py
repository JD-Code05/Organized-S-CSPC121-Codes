#Set(Lottery)
#BCS13 - Ubungen

import random

wSets = set()

while len(wSets)<6:
    wSets.add(random.randint(1, 51))
    
print(f"Winning Numbers: {wSets}")

print("Enter 6 Digit: ")

uSets = set()

while len(uSets)<6:
    num = int(input(""))
    if num < 1:
        print("Invalid")
    elif num in uSets:
        print("Duplicate")
    elif num > 50:
            print("Exceed 50")
    else:
        uSets.add(num)
            
print(uSets)
if uSets == wSets:
    print("Congratulations!!!You win")
else:
    print("Better Luck Next Time!")