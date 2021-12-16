from datetime import date

today = date.today().year
name = input('Enter Your Name : ')
age = int(input('Enter Your Age : '))
b_year = today - age
c_year = b_year + 100
print('Hey {} , You will be 100 years old by the year {}. P.S. The World will end much before that. :) '.format(name, c_year))


