#مثال: عددی را ب طور چیش فرض در ذهن خود نگه دارد کاربر حدس بزند
import random
number_of_guesse=0
guess_tries=number_of_guesse+1
answer=random.randint(0,99)
while True:
    user_number=int(input('enter your number'))
    
    if user_number>answer:
        print('your number is bigger')
    
    elif user_number<answer:
        print('your number is lower')
   
    else:
        print('welldone,you are right')
        break

if user_number == answer:
    number_of_guesse = number_of_guesse + 1
    print('You guessed the number in ' + str(number_of_guesse) + ' tries!')