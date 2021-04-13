# This program will ask for your grade scores,
# and will calculate and display the high, low,
# and average for the entered scores.


def get_scores():
    print("Enter scores, stops when negative value is entered.")
    scores = []
    while True:
        print("Enter score:")
        n = int(input())
        if n < 0:
            break
        else: scores.append(n)

    return scores
        
    
def calculate_maximum(scores):
    maximum = scores[0]
    for index in range(0, len(scores)):
        if maximum < scores[index]:
            maximum = scores[index]            
    return maximum


def calculate_minimum(scores):
    minimum = scores[0]
    for index in range(1, len(scores)):
        if minimum > scores[index]:
            minimum = scores[index]
            
    return minimum


def calculate_average(scores):
    total = 0
    for index in range(len(scores)):
        total += scores[index]
        average = sum(scores) / len(scores)
        
    return average


def display_results(maximum, minimum, average):
    print("The average for entered scores is", average)
    print("The highest score from entered scores is", maximum)
    print("The lowest score from entered scores is", minimum)
    
    
def main():
    scores = get_scores()    
    maximum = calculate_maximum(scores)
    minimum = calculate_minimum(scores)
    average = calculate_average(scores)    
    display_results(maximum, minimum, average)


main()
