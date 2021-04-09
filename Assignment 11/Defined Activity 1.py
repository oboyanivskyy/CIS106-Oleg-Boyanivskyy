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


def calculate_month_dates(year):
    if (year % 400) == 0:
        monthdates = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    elif (year % 100) == 0:
        monthdates = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    elif (year % 4) == 0:
        monthdates = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        monthdates = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
    return monthdates


def calculate_month_name(month):
    months = ["January", "February", "March",
              "April", "May", "June",
              "July", "August", "September",
              "October", "November", "December"]

    if month < 1 or month > 12:
        return "Unknown"
    
    return months[month - 1]


def calculate_month_days(year, month):
    if month < 1 or month > 12:
        return "Unknown"

    month_dates = calculate_month_dates(year)
    return month_dates[month - 1]


def display_results(month, year, month_days):
    print(month, year, "has", month_days, "days")
    

def main():
    while True:
        year = get_year()
        if(year < 1582):
            break

        month = get_month()
        if(month > 12 or month < 1):
            break

        month_name = calculate_month_name(month)
        month_days = calculate_month_days(year, month)
        display_results(month_name, year, month_days)
   
   
main()
