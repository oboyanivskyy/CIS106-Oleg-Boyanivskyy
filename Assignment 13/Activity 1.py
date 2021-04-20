# This program will ask the user for their
# first name and last name, and then parse them
# out.


def get_name():
    while True:
        print("Enter name (first last):")
        name = input()
        index = name.find(" ")
        if index >= 0:
            break
    return name


def get_first(name):
    index = name.find(" ")
    if index < 0:
        first = ""
    else:
        first = name[0]
        first = first.upper()
    return first


def get_last(name):
    index = name.find(" ")
    if index < 0:
        last = ""
    else:
        last = name[index + 1:]
        last = last.strip()
        last = last.capitalize()
    return last


def display_name(first, last):
    print(f"{last}, {first}.")


def main():
    name = get_name()
    last = get_last(name)
    first = get_first(name)
    display_name(first, last)
 
 
main()