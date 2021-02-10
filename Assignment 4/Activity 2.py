# This program will display your age in months, days, hours, and seconds.

print("Enter your age in years")

years = float(input())

months = years * 12
days = years * 365
hours = days * 24
seconds = hours * 3600

print("You are " + str(years) + " years, " + str(months) + " months, ")
print(+ str(days) + " days, " + str(hours) + " hours, " + str(seconds) + " seconds old ")

