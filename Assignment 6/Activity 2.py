# This updated program will take your age,
# and display your age in months, days, hours,
# and seconds.


def getAge():
    print("Enter your age in years.")
    age = float(input())
    return age


def calcMonths(age):
    months = age * 12
    return months


def calcDays(age):
    days = age * 365
    return days


def calcHours(days):
    hours = days * 24
    return hours


def calcSeconds(hours):
    seconds = hours * 60 * 60
    return seconds


def displayResult(months,days,hours,seconds):
    print("You are " + str(months) + " months, ")
    print(str(days) + " days, ")
    print(str(hours) + " hours, and ")
    print(str(seconds) + " seconds old ")
    
def main():
    age = getAge()
    months = calcMonths(age)
    days = calcDays(age)
    hours = calcHours(days)
    seconds = calcSeconds(hours)
    displayResult(months,days,hours,seconds)
    
    
    
main()


