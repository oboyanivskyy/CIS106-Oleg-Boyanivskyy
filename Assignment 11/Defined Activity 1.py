# This program will ask for a year and month number,
# and then look up the corresponding month name and number
# of days and display that information.


def get_month():
    print("Enter the month number you wish to look up:")
    month = int(input())

    return month


def get_year():
    print("Enter the year you wish to look up:")
    year = int(input())

    return year


def calculate_monthdates(year):
    if (year % 400) == 0:
        monthdates = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    elif (year % 100) == 0:
        monthdates = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    elif (year % 4) == 0:
        monthdates = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        monthdates = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
    return monthdates


def display_array(month, year, monthdates):
    months = ["January", "February", "March",
              "April", "May", "June",
              "July", "August", "September",
              "October", "November", "December"]
    month = month - 1
    print("There are", monthdates[month], "days",
        "in the month of", months[month], "in", year)
    

def main():
    while True:
        month = get_month()
        if(month > 12 or month < 1):
            break
        year = get_year()
        if(year < 1582):
            break
        monthdates = calculate_monthdates(year)
        display_array(month, year, monthdates)
   
   
main()