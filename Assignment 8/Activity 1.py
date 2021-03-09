def get_value():
    print("Enter your value")
    value = int(input())
    
    return value

def get_expressions():
    print ("Enter how many expressions")
    expressions = int(input())
    
    return expressions

def calculate_expressions(value, expressions):
    increment = 1
    count = 0
    while count < expressions:
        count = count + increment
        print(str(value) + " * " + str(count) + " = " + str(value * count))

# Main
# This program will ask for how many expressions you want for a given value,
# and calculate them.
value = get_value()
expressions = get_expressions()
calculate_expressions(value, expressions)