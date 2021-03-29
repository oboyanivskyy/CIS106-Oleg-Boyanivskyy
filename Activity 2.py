# This program will ask for the amount of grade scores
# you would like to enter and then will calculate and,
# display them to you.


def get_amount():
    print("How many scores would you like to enter?")
    amount = int(input())
    
    return amount


def get_score():
    print("Enter your score:")
    score = int(input())
    
    return score
        
        
def calculate_average(amount):
    result = 0
    for increment in range(1, amount + 1, 1):
        score = get_score()
        result = result + score
    result = result / amount
    
    return result
        
        
def display_result(result):
    print("Your average for all scores is " + str(result))
    
    
def main():
    amount = get_amount()
    result = calculate_average(amount)
    display_result(result)


main()