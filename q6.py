x = input('Please enter a string. ')

y = x[0:].lower()
z = x[::-1].lower()

if y == z:
    print('{} is a palindrome.'.format(x))
else:
    print('{} is not a palindrome.'.format(x))    




