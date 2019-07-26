#!/usr/bin/env python3

import math

def triangle():
     base =  float(input("Give base of the triangle:"))
     height = float(input("Give height of the triangle:"))
     area = base*height*0.5
     print(f"The area is {area:.6f}")  

def rectangle():
    width =  float(input("Give width of the rectangle:"))
    height = float(input("Give height of the rectangle:"))
    area = width*height
    print(f"The area is {area:.6f}")

def circle():
    radius = float(input("Give radius of the circle:"))
    area = math.pi*radius**2
    print(f"The area is {area:.6f}")
        


def main():
    # enter you solution here
    while(True):
        userInput = input("Choose a shape (triangle, rectangle, circle):")
        if userInput == "":
            break
        elif userInput == "triangle":
            triangle()
        elif userInput == "rectangle":
            rectangle()
        elif userInput == "circle":
            circle()
        else:
            print("Unknown shape!")               

    pass
if __name__ == "__main__":
    main()
