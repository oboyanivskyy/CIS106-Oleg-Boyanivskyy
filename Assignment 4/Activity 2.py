# This program will display your age in months, days, hours, and seconds.

print("Enter your age in years")
years = float(input())

months = years * 12
days = years * 365
hours = days * 24
seconds = hours * 60 * 60

print("You are " + str(months) + " months ")
print(str(days) + " days ")
print(str(hours) + " hours ")
print(str(seconds) + " seconds old ")
