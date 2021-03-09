def getvalue():
    print("Enter your value")
    value = int(input())
    
    return value

def whileloop(value):
    increment = 1
    count = 0
    while count <= 4:
        count = count + increment
        print(str(value) + " * " + str(count) + " = " + str(value * count))

# Main
# This program will generate a list of 5 multiplication expressions for a given value.
value = getvalue()
whileloop(value)
