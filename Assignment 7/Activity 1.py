def calculate_dogyears(hyears):
    if hyears > 2:
        years = 2 * 10.5 + (hyears - 2) * 4
    else:
        years = hyears * 10.5
    
    return years

def display_results(years, name):
    print(name + " is " + str(years) + " years old in dog years.")

def get_age():
    print("How old is your dog in human years?")
    hyears = int(input())
    
    return hyears

def get_name():
    print("What is the name of your dog?")
    name = input()
    
    return name

# Main
# This program will input your dog's name and age, and convert it to dog years.
name = get_name()
hyears = get_age()
years = calculate_dogyears(hyears)
display_results(years, name)
