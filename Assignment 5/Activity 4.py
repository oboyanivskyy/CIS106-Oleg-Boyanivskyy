def calculatePara():
    print("What is the base of the parallelogram?")
    base = int(input())
    print("What is the height of the parallelogram?")
    height = int(input())
    parallel = base * height
    
    return parallel

def calculateRect():
    print("What is the width of the rectangle?")
    width = float(input())
    print("What is the height of the rectangle?")
    height = float(input())
    rectangle = width * height
    
    return rectangle

def calculateTrian():
    print("What is the base of the triangle?")
    base = int(input())
    print("What is the height of the triangle?")
    height = int(input())
    triangle = float(1) / 2 * base * height
    
    return triangle

def displayArea(rectangle, triangle, parallel):
    print("The area of the rectangle is " + str(rectangle))
    print("The area of the triangle is " + str(triangle))
    print("The area of the parallelogram is " + str(parallel))

# Main
# This program will calculate area for a triangle, rectangle, and parallelogram
rectangle = calculateRect()
triangle = calculateTrian()
parallel = calculatePara()
displayArea(rectangle, triangle, parallel)
