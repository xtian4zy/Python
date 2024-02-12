'''
Write a program to compute the areas of three different shapes. Prompt for the necessary information, then compute and display the area, as follows:

Make sure that your program can appropriately handle decimal values as well as whole numbers.

Square—The area is the length of a side squared.

Rectangle—The area is the length multiplied by the width.

Circle—The area is Pi (you can use 3.14) multiplied by the radius squared.
'''

square_side = float(input('Enter the Square side:'))


square_area = square_side ** 2
print('The area of the Saquare is ', square_area)

rectangle_len = float(input('Enter the Rectangle Length:'))
rectangle_width = float(input('Enter the Rectangle Width:'))
rect_area = rectangle_width * rectangle_len
print('The area of the rectangle is ', rect_area)

circle_radius = float(input('Enter the Circle radius:'))
circle_area = 3.14 * (circle_radius ** 2)
print('The area of the circle is ', circle_area)