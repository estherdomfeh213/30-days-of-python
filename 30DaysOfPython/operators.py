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

