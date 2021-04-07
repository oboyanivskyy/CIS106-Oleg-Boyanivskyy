# This program will ask for a year and month number,
# and then look up the corresponding month name and number
# of days and display that information.


def get_month():
    print("Enter the month number you wish to look up")
    month = int(input())

    return month


def get_year():
    print("Enter the year you wish to look up")
    year = int(input())

    return year


def calculate_result(month, year):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    if (year % 4) == 0 and (year % 400) == 0:
        monthdates = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        monthdates = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        

def display_result(month, year, result):
    print("The month of " + month + "has " + result " days in the year of " + year)
    

def main():
    while True: month < 13 or month > 0 or year > 1582
        month = get_month()
        year = get_year()
        result = calculate_result(month, year)
        display_result(month, year, result)
        if not:
            break
        
main()