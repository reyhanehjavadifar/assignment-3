
import random 
dice = []

while True:
    dice.append(random.randint(1,6))
    if 6 in dice:
        print('\nsum numbers : ',str(sum (dice)))
        print('list number : ',dice)
        break
    else:
        continue

