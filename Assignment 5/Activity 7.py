def calculateDogYears(hyears):
    years = hyears * 7
    
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
