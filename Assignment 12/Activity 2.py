# This program will attempt to guess a number in your head,
# between 0 to 100.


def calculate_number():
    array = []
    start = 50
    start_range = 0
    end_range = 100
    while True:
        response = get_response(start)
        if response == str("e"):
            array.append(response)
            display_result(array, response)
            break
        elif response == str("h"):
            array.append(response)
            start_range = start
            start = round((start_range + end_range) / 2)
        elif response == str("l"):
            array.append(response)
            end_range = (end_range / 2)
            start = round((start_range + end_range) / 2)
        else:
            print("Invalid Response")
        

def get_response(start):
    print("Is your number higher, lower, or equal to", start, "?")
    response = input(float())
    
    return response

    
def display_result(array, response):
    print("I guessed your number!")
    print("These are the attempts it took me:", array)


def main():
    calculate_number()
    
    
main()