# This updated program asks the user for their hours per week,
# and rate, then calculates weekly, monthly, and annual pay,
# calculates overtime, and displays the result.

    
def get_hours():
    print("Enter Hours Worked Per Week")
    hours = float(input())
    return hours


def get_rate():
    print("Enter Your Rate Per Hour")
    rate = float(input())
    return rate


def calculate_weekly(rate, hours):
    if hours > 40:
        weekly = (rate * hours) + (hours - 40) * (0.5 * rate)
    else:
        weekly = rate * hours
    return weekly


def calculate_monthly(weekly):
    monthly = weekly * 4
    return monthly


def calculate_annual(weekly):
    annual = weekly * 52
    return annual


def display_result(weekly, monthly, annual):
    print("Your Weekly Pay is $" + str(weekly))
    print(" Monthly Pay is $" + str(monthly))
    print(" Yearly Pay is $" + str(annual))


def process_pay():
    hours = get_hours()       
    rate = get_rate()
    weekly = calculate_weekly(rate, hours)
    monthly = calculate_monthly(weekly)
    annual = calculate_annual(weekly)
    display_result(weekly, monthly, annual)


def loop_end(answer):
    print("Thank you for using the program")
    
    
def main():
    while True:
        process_pay()
        print("Type yes to make another calculation.")
        answer = str(input())
        if not(answer == "yes"):
            break


main()
