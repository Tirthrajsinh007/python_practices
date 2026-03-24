# 2. Create functions to calculate
# a. Area of a rectangle = width * length
# b. Area of a triangle = ½ * Height * Base
# c. Area of a circle = pi*r*r
import math

def area_of_rectangle():
    width = float(input("Enter Width :"))
    length = float(input("Enter Lenght :"))
    return print(width*length)
def area_of_triangle():
    height = float(input("Enter Height :"))
    base = float(input("Enter Base :"))
    return print(0.5*height*base)
def area_of_circle():
    
    r = float(input("Enter Radius :"))
    return print(math.pi*r*r)

area_of_rectangle()
area_of_circle()
area_of_triangle()