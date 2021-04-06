# This program will ask for your grade scores,
# and will calculate and display the high, low,
# and average for the entered scores.


def get_amount():
    print("How many scores would you like to enter?")
    amount = int(input())
    
    return amount


def get_scores(amount):
    array = [None] * amount
    for index in range(len(array)):
        print("Enter your score: ")
        
    
def max(array):
    maximum = array[0]
    for index in range(1, len(array)):
        if maximum < array[index]:
            maximum = array[index]
    return maximum


def min(array):
    minimum = array[0]
    for index in range(1, len(array)):
        if minimum > array[index]:
            minimum = array[index]
    return minimum


def avg(array, amount):
    total = 0
    for index in range(len(array)):
        total += array[index]
        average = total / amount
    return average
    
    
def main():
    amount = get_amount()
    scores = get_scores(amount)
    
    maximum = max(scores)
    minimum = min(scores)
    average = avg(scores)
    
    print("Average for entered scores is: " + str(average))
    print("Highest entered score is: " + str(maximum))
    print("Lowest entered score is: " + str(minimum))
    
    
main()