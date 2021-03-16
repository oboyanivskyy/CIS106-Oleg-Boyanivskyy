# This program will calculate expressions you want for a given value,
# until you want it to stop.


def get_value():
    print("Enter your value, write -1 to stop.")
    value = int(input())
    
    return value


def calculate_expressions(value):
    increment = 1
    count = 0
    while True:
        count = count + increment        
        display_expressions(value, count)
        get_value()
        if not(value == -1): break


def display_expressions(value, count):
    print(str(value) + " * " + str(count) + " = " + str(value * count))


def main():
    value = get_value()
    count = calculate_expressions(value)


main()