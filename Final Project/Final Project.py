# This program will read data from w3schools.com,
# and build parallel array for catalog items, as well as
# display the menu items.


def read_data(filename):
    count = 0
    item(count) = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
def main():
    filename = "cd_catalog.xml"
    try:
        read_data(filename)
    except TypeError:
        print("Error: Missing or bad data")
    except ValueError:
        print("Error: Missing or bad data")
    except IndexError:
        print("File is empty")
    except FileNotFoundError:
        print("File is missing")


main()
