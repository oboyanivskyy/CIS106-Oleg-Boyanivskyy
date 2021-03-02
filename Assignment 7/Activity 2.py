def calculateDogYears(hyears):
    if hyears > 2:
        years = (2 * 10.5)+(hyears-2)*4
    elif hyears <= 2:
        years = hyears * 10.5
    
    return years

def displayResults(years, name):
    print(name + " is " + str(years) + " years old in dog years.")

def getAge():
    print("How old is your dog in human years?")
    hyears = int(input())
    
    return hyears

def getName():
    print("What is the name of your dog?")
    name = input()
    
    return name

# Main
# This program will input your dog's name and age, and convert it to dog years.
name = getName()
hyears = getAge()
years = calculateDogYears(hyears)
displayResults(years, name)
