def get_value():
    print("Enter your value")
    value = int(input())
    
    return value

def while_loop(value):
    increment = 1
    count = 0
    while count <= 4:
        count = count + increment
        print(str(value) + " * " + str(count) + " = " + str(value * count))

# Main
# This program will generate a list of 5 multiplication expressions for a given value.
value = get_value()
while_loop(value)
