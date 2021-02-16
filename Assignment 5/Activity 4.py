# This program will calculate area for a triangle, rectangle, and parallelogram

def getTriangle():
    print("Enter the base of the triangle")
    base = int(input())
    print("Enter height of the triangle")
    height = int(input())
    triangle = 0.5 * base * height
    
    return triangle

def getRectangle():
    print("Enter the height of the rectangle")
    height = int(input())
    print("Enter the width of the rectangle.")
    width = int(input())
    rectangle = width * height
    
    return rectangle

def getParallel():
    print("Enter the base of the parallelogram")
    base = int(input())
    print("Enter the vertical height of the parallelogram")
    height = int(input())
    parallel = base * height
    
    return parallel

# Main

triangle = getTriangle()
rectangle = getRectangle()
parallel = getParallel()

print("Area of triangle = " + str(triangle))
print("Area of rectangle = " + str(rectangle))
print("Area of parallelogram = " + str(parallel))
