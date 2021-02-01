# This program will calculate weekly, monthly, and annual gross pay.
print("Enter Hours Worked Per Day:")
hours = float(input())
print("Enter Rate Per Hour:")
rate = float(input())
totalweek = rate * hours * 5
totalmonth = totalweek * 4
totalyear = totalmonth * 12
print("Weekly Pay is" + str(totalweek) + "Monthly Pay is" + str(totalmonth) + "Yearly Pay is" + str(totalyear))
