# This program will ask for the amount of grade scores
# you would like to enter and then will calculate and,
# display them to you.


def get_amount():
    print("How many scores would you like to enter?")
    amount = int(input())
    
    return amount


def get_newamount():
    print("How many scores would you like to enter?")
    newamount = int(input())
    
    return newamount


def get_score():
    print("Enter your score:")
    score = int(input())
    
    return score
        
        
def get_newscore():
    print("Enter your score:")
    newscore = int(input())
    
    return newscore


def get_answer():
    print("Would you like to enter more scores? Type yes or hit enter to calculate")
    answer = str(input())
    
    return answer


def calculate_average(amount):
    result = 0
    newresult = 0
    for increment in range(1, amount + 1, 1):
        score = get_score()
        result = result + score
    while True:
        answer = get_answer()
        result = result / amount
        if not(answer == "yes"): break        
        newamount = get_newamount()
        for increment in range(1, newamount + 1, 1):
            newscore = get_newscore()
            newresult = newresult + newscore
            result = (newresult + result) + (newscore + score)
            amount = newamount + amount
        result = result / amount
            
    return result
        
        
def display_result(result):
    print("Your average for all scores is " + str(result))
    
    
def main():
    amount = get_amount()
    result = calculate_average(amount)
    display_result(result)


main()