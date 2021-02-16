#This program will display your dog's name and calculcate their age in dog years.

def getName():
    print("What is the name of your dog?")
    name = input()
    
    return name

def getYears():
    print("How old is your dog in human years?")
    hyears = int(input())
    years = hyears * 7
    
    return years

# Main
name = getName()
years = getYears()
print(name + " is " + str(years) + " years old in dog years.")
