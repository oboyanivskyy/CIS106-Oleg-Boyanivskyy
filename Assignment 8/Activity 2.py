# This program will take your grade scores,
# add it to a total, calculate, and display,
# the average for the entered scores.


def get_amount():
    print("How many scores do you want to enter?")
    amount = int(input())
    
    return amount


def get_score(count):
    print("Enter score " + str(count))
    score = int(input())
    
    return score


def calculate_score(amount):
    count = 1
    totalscore = 0
    while count <= amount:
        score = get_score(count)
        count = count + 1
        totalscore = totalscore + score
    
    return totalscore


def calculate_average(amount, totalscore):
    total = totalscore / amount
    
    return total


def display_average(total):
    print("Your average for entered scores is " + str(total))
    
    
def main():
    amount = get_amount()
    totalscore = calculate_score(amount)
    total = calculate_average(amount, totalscore)
    display_average(total)
    
    
main()