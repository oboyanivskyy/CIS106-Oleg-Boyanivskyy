# This updated program asks the user for their hours per week,
# and rate, then calculates weekly, monthly, and annual pay,
# and displays the result.

    
def getHours():
    print("Enter Hours Worked Per Week")
    hours = float(input())
    return hours


def getRate():
    print("Enter Your Rate Per Hour")
    rate = float(input())
    return rate


def calculateWeekly(rate,hours):
    weekly = rate * hours
    return weekly


def calculateMonthly(weekly):
    monthly = weekly * 4
    return monthly


def calculateAnnual(weekly):
    annual = weekly * 52
    return annual


def displayResult(weekly,monthly,annual):
    print("Your Weekly Pay is $" + str(weekly))
    print(" Monthly Pay is $" + str(monthly))
    print(" Yearly Pay is $" + str(annual))
    
    
def main():
    hours = getHours()
    rate = getRate()
    weekly = calculateWeekly(rate,hours)
    monthly = calculateMonthly(weekly)
    annual = calculateAnnual(weekly)
    displayResult(weekly,monthly,annual)


main()
    
    
    
    
