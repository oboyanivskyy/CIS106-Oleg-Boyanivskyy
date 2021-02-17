def calculateRectArea(rectheight, width):
    rectangle = rectheight * width
    
    return rectangle

def calculateTriangleArea(base, height):
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
    rectheight = int(input())
    
    return rectheight

def getWidth():
    print("What is the width of the rectangle?")
    width = int(input())
    
    return width

# Main
# This program will calculate area for a triangle and rectangle.
base = getBase()
height = getHeight()
triangle = calculateTriangleArea(base, height)
width = getWidth()
rectheight = getRectHeight()
rectangle = calculateRectArea(width, rectheight)
displayResults(triangle, rectangle)
