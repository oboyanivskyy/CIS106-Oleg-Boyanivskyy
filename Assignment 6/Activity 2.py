# This updated program will take your age,
# and display your age in months, days, hours,
# and seconds.


def get_age():
    print("Enter your age in years.")
    age = float(input())
    return age


def calc_months(age):
    months = age * 12
    return months


def calc_days(age):
    days = age * 365
    return days


def calc_hours(days):
    hours = days * 24
    return hours


def calc_seconds(hours):
    seconds = hours * 60 * 60
    return seconds


def display_result(months, days, hours, seconds):
    print("You are " + str(months) + " months, ")
    print(str(days) + " days, ")
    print(str(hours) + " hours, and ")
    print(str(seconds) + " seconds old ")


def main():
    age = get_age()
    months = calc_months(age)
    days = calc_days(age)
    hours = calc_hours(days)
    seconds = calc_seconds(hours)
    display_result(months, days, hours, seconds)
    
      
main()