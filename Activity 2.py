# This program will attempt to guess a number in your head,
# between 0 to 100.


def start_game():
    print("Think of a number between 0 to 100.")
    print("Once you have your number, press enter to continue.")
    start = input(str())
    
    return start


def find_guess():
    array = []
    start = 50
    start_range = 0
    end_range = 100
    while True:
        print("Is your number higher, lower, or equal to", start, "?")
        response = input(float())
        if response == str("equal"):
            array.append(response)
            display_result(array, response)
            break
        elif response == str("higher"):
            array.append(response)
            start_range = start
            start = round((start_range + end_range) / 2)
        elif response == str("lower"):
            array.append(response)
            end_range = (end_range / 2)
            start = round((start_range + end_range) / 2)
        else:
            print("Invalid Response")
        
        
def display_result(array, response):
    print("I guessed your number!")
    print("These are the attempts it took me:", array)


def main():
    start = start_game()
    answer = find_guess()
    
    
main()