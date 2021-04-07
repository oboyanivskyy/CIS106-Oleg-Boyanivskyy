# This program will ask for your grade scores,
# and will calculate and display the high, low,
# and average for the entered scores.


def get_amount():
    print("How many scores would you like to enter?")
    amount = int(input())
    
    return amount


def get_scores(amount):
    scores = [None] * amount
    for index in range(len(scores)):
        print("Enter your score: ")
        index = int(input())
        
        scores.append(index)
        
    return scores
        
    
def max(scores):
    maximum = scores[0]
    for index in range(0, len(scores)):
        if maximum < scores[index]:
            maximum = scores[index]            
    return maximum


def min(scores):
    minimum = scores[0]
    for index in range(1, len(scores)):
        if minimum > scores[index]:
            minimum = scores[index]
            
    return minimum


def avg(scores, amount):
    total = 0
    for index in range(len(scores)):
        total += scores[index]
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