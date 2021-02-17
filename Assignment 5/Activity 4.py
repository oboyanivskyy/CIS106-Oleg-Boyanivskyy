def calculateRectArea():
    width = getWidth()
    height = getRectHeight()
    rectangle = width * height
    
    return rectangle

def calculateTriangleArea():
    base = getBase()
    height = getHeight()
    triangle = base * height * (float(1) / 2)
    
    return triangle

def displayResults(triangle, rectangle):
    print("The area of the triangle is " + str(triangle))
    print("The area of the rectangle is " + str(rectangle))

def getBase():
    print("What is the base of the triangle?")
    base = int(input())
    
    return base

def getHeight():
    print("What is the height of the triangle?")
    height = int(input())
    
    return height

def getRectHeight():
    print("What is the height of the rectangle?")
    height = int(input())
    
    return height

def getWidth():
    print("What is the width of the rectangle?")
    width = int(input())
    
    return width

# Main
# This program will calculate area for a triangle and rectangle.
rectangle = calculateRectArea()
triangle = calculateTriangleArea()
displayResults(triangle, rectangle)
