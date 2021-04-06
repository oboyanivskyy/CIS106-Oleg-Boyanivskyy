# This program will ask for a year and month number,
# and then look up the corresponding month name and number
# of days and display that information.


def get_month():
    print("Enter the month number you wish to look up")
    month = int(input())
    if 12 < month < 0:
        print("Please enter a valid month number")
    else:
    
        return month


def get_year():
    print("Enter the year you wish to look up")
    year = int(input())
    if year < 1582:
        print("Please enter a year higher than 1582")
    else:
    
        return year


def calculate_result(month, year):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    monthdates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    if year / 4 or year / 400:
        dates = [January = 31, Febraury = 29, March = 31, April = 30, May = 31, June = 30, July = 31, August = 31, September = 30, October = 31, November = 30, December = 31]
    else year / 100:
        dates = [January = 31, Febraury = 28, March = 31, April = 30, May = 31, June = 30, July = 31, August = 31, September = 30, October = 31, November = 30, December = 31]
        

def display_result(month, year, result):
    print("The month of " + month + "has " + result " days in the year of " + year)
    print("Would you like to do another calculation? Yes or No?")
    answer = str(input())
    if answer == "yes" or answer == "Yes"
        process_result()
    elif answer == "no" or answer == "No"
        print("Thank you for using the program")
    else:
        print("Invalid response")
    
    
def process_result():
    month = get_month()
    year = get_year()
    result = calculate_result(month, year)
    display_result(month, year, result)
    

def main():
    process_result()


main()