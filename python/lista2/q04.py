import random
dice = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0, 
    6: 0
    }

for i in range (20):
    throw = random.randint(1,6)
    dice[throw] +=1

for num, count in dice.items():
    print (f"the number {num} count is {count}")