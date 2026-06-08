# Day 2: 30 Days of Python programming

first_name = 'Miley'
last_name = 'Chris'
full_name = 'Miley Chris'
country = 'Belgium'
city = 'Brussels'
age = 30
year = 2024
is_married = False
is_true = True
is_light_on = True
fav_food, music, color, vacation = 'pasta', 'pop', 'pink', 'singapore'

# Exercises: Level 2
# 1: Check the data type of all your variables using type() built-in function.
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(fav_food))
print(type(music))
print(type(color))
print(type(vacation))   

# 2: Using the len() built-in function, find the lenght of your first name.
print(len(first_name))

# 3: Compare the length of your first name and your last name.
compare_firstname_lastname = len(first_name) == len(last_name)
print(compare_firstname_lastname)

# 4: Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

# 5: Add num_one and num_two ad assign the value to a variable total
total = num_one + num_two

# 6: Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
print(diff)
# 7: Multiply num_two and num_one abd assign the value to a variable product
product = num_two * num_one
print(product)

# 8: Divide num_one by num_two abd assign the value ti a variable division
division = num_one / num_two
print(division)

# 9: Use modulus division to find num_two divided by num_one and assign the value to a variable reminder
reminder = num_two % num_one
print(reminder)

# 10: Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
print(exp)

# 11: Find the floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print(floor_division)

# 12: The radius of a circle is 30 meters.
"""
The radius of a circle is 30 meters.
i. Calculate the area of a circle and assign the value to a variable name of area_of_circle
ii. Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
iii. Take radius as user input and calculate the area.
"""
# i: formula for calculating the area of a circle: A=πr2, where pi= 3.14159265359
radius = 30
pi = 3.14159265359
area_of_circle = pi * radius ** 2
print(area_of_circle)

# ii: formula for calculation the circumference of a circle: C=2πr
circum_of_circle = 2 * pi * radius
print(circum_of_circle)

#iii: take user input to calculate the area of a circle
user_radius = input("Enter radius: ")
calc_radius = pi * int(user_radius) ** 2
print(calc_radius)

# 13: Use the built-in input function to get first name, last name,
# country and age from a user and store the value to their corresponding variable names
firstname = input("Enter first name: ")
lastname = input("Enter last nam: ")
country = input("Enter country: ")
age = input("Enter age: ")
print(firstname, lastname, country, age)

# 14: Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

"""python3                 
Python 3.14.3 (main, Feb  3 2026, 15:32:20) [Clang 17.0.0 (clang-1700.6.3.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> help('keywords')

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 

>>> 
"""