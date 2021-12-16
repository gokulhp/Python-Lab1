import random

x = (random.randrange(0,9,1))

y = int(input('Guess an integer between 0 and 9. : '))

if x == y:
    print('You guessed right..!')
elif y > x:
    print('Too high.')
elif y < x:
    print('Too low.')        

