# This program will calculate weekly, monthly, and annual gross pay.
print("Enter Hours Worked Per Week:")
hours = float(input())
print("Enter Rate Per Hour:")
rate = float(input())
totalweek = rate * hours
totalmonth = totalweek * 4
totalyear = totalweek * 52
print("Weekly Pay is " + str(totalweek) + " Monthly Pay is " + str(totalmonth) + " Yearly Pay is " + str(totalyear))
