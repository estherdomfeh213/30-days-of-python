# Day 3: Exercises

age = 76
height_cm = 172
complex_num = 1 + 1j

# Write a script that prompts the user to enter
# base and height of the triangle and calculate an
# area of this triangle (area = 0.5 x b x h).
base = input("Enter base: ")
height = input("Enter height: ")
area_triangle = 0.5 * int(base) * int(height)
print("The area of the triangle is: ", area_triangle )

# 5. Write a script that prompts the user to enter side a,
# side b, and side c of the triangle.
# Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))
perimeter = side_a + side_b + side_c
print("The perimeter of the triangle is ", perimeter)

# 6. Get length and width of a rectangle using prompt.
# Calculate its area (area = length x width)
# and perimeter (perimeter = 2 x (length + width))
rec_length = float(input("Enter length: "))
rec_width  = float(input("Enter width: "))
area_of_rec = rec_length * rec_width
print("The area of the of the rectangle is ", area_of_rec)
perimeter_of_rec = 2 * (rec_length * rec_width)
print("The perimeter of the triangle is ", perimeter_of_rec)

# 7. Get radius of a circle using prompt.
# Calculate the area (area = pi x r x r)
# and circumference (c = 2 x pi x r) where pi = 3.14.
circle_radius = float(input("Enter radius: "))
pi = 3.14
area_circle = pi * circle_radius**circle_radius
circumference_circle = 2 * pi * circle_radius
print("The the area of the circle is ", area_circle)
print("The circumference of the circle is ", circumference_circle)

# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope = 2
y_intercept = -2
x_intercept = -y_intercept / slope
print(f"Slope: {slope}")
print(f"X-intercept: ({x_intercept}, 0)")
print(f"Y-intercept: (0, {y_intercept})")


# 9. Slope is (m = y2-y1/x2-x1). Find the slope and
# Euclidean distance between point (2, 2) and point (6,10)

# coordinates for the two points
x1, y1 = 2, 2
x2, y2 = 6, 10

slope = (y2 - y1) /(x2 - x1)

# calculate the Euclidean distance
# nOTE: **2 means squared, and **0.5 means square root
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print(f"Slope: {slope}")
print(f"Euclidean Distance: {distance:.4f}")

# 10. Compare the slopes in tasks 8 and 9.
print("Slope equal to distance? ",slope == distance)

# 11.  Calculate the value of y (y = x^2 + 6x + 9).
# Try to use different x values and figure out at what x value y is going to be 0.
x_values = [-5, -4, -3, -2, -1, 0]

print("Testing x values:")
print("--------------")

for x in x_values:
    y = x**2 + 6*x + 9
    print(f"When x = {x}, y = {y}")

    if y == 0:
        print(f"Found it! y is 0 when x = {x}")


# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len('python') != len('dragon'))

# 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python', 'on' in 'dragon')

# 14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon' in " I hope this course is not full of jargon")


# 15  There is no 'on' in both dragon and python
result = ('on' in 'python') != ('on' in 'dragon')
print(f"There is on 'on' in both dragon and python: {result}  ")

# 16. Find the length of the text python and convert the value to float and convert it to string
py_len = len('python')
result1 = float(py_len)
result2 = str(result1)
print("This is a string: ",type(result2))

# 17. Even numbers are divisible by 2 and the remainder is zero.
# How do you check if a number is even or not using python?

number = 14

# check if the reminder is exactly 0
if number % 2 == 0:
    print(f"{number} is an EVEN number.")
else:
    print(f"{number} is an ODD number.")


# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

print("Is the floor division equal to convert int? ",7 / 3 == int(2.7))

# 19. Check if type of '10' is equal to type of 10
print("Is '10' equal to 10? ", type('10') == type(10) )

# 20 Check if int('9.8') is equal to 10
"""
nOTE: python int() function cannot convert text with a decimal point directly into integer
convert text to float first , and turn that float into an int. 
"""
conversion_int = int(float('9.8'))
print("int('9.8') equal to 10?", type(conversion_int) == type(10))

# 21.Write a script that prompts the user to enter hours and rate per hour.
# Calculate pay of the person?
hours_worked = float(input("Enter hours: "))
hourly_rate = float(input("Enter rate per hour: "))
weekly_earnings = hours_worked * hourly_rate
print(f"Your weekly earning is ", weekly_earnings)

# 21. Write a script that prompts the user to enter number of years.
# Calculate the number of seconds a person can live. Assume a person can live hundred years
years_input = input("Enter number of years you have lived: ")
years = int(years_input)

max_years = 100

if years > max_years:
    print(f"Note: Assuming a maximum lifespan of {max_years} years. Adjusting calculation to 100.")
    years = max_years

seconds_in_a_year = 365 *  24 * 60 * 60
total_seconds = years * seconds_in_a_year
print(f"You have lived for {total_seconds} seconds.")


# 23. Write a Python script that displays the following table

print("1 1 1 1 1")

for i in range (2, 6):
    col1 = i
    col2 = i**0
    col3 = i**1
    col4 = i**2
    col5 = i**3

    print(f"{col1} {col2} {col3} {col4} {col5}")