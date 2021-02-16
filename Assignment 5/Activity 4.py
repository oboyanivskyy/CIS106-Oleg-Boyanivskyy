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

def getParallelogram():
    print("Enter the base of the parallelogram")
    base = int(input())
    print("Enter the vertical height of the parallelogram")
    height = int(input())
    parallelogram = base * height
    
    return parallelogram

# Main
# This program will calculate area for a triangle, rectangle, and parallelogram
triangle = getTriangle()
rectangle = getRectangle()
parallelogram = getParallelogram()
print("Area of triangle is " + str(triangle) + ", Area of rectangle is " + str(rectangle) + ", and Area of the parallelogram is " + str(parallelogram))
