def calculate_expression(value, expression):
    for increment in range(1, expression + 1, 1):
        display_result(value, increment)


def display_result(value, increment):
    print(str(value) + " * " + str(increment) + " = " + str(value * increment))


def get_expression():
    print("Enter how many expressions you would like to calculate.")
    expression = int(input())
    
    return expression


def get_value():
    print("Enter the value you would like to use for the expression.")
    value = int(input())
    
    return value


# Main
# This program will ask for a value and amount of expressions, and will display those as multiplcation expressions.
value = get_value()
expression = get_expression()
calculate_expression(value, expression)
