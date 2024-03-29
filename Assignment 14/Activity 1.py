# This program will copy a list of names and grade scores
# into a text file and then display high, low, and average
# scores.
import os
import sys


def read_file(filename):
    scores = []
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                print(line)
                numeric_filter = filter(str.isdigit, line)
                line = "".join(numeric_filter)
                if line == "":
                    pass
                else:
                    scores.append(line)
        scores = list(map(int, scores))
        print(scores)
    except:
        print("Error reading", filename)
        print(sys.exc_info()[1])
    
    return scores


def calculate_max(scores):
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
        average = str(round(average, 2))
        
    return average


def display_results(maximum, minimum, average):
    print("The average score is", average)
    print("The highest score is", maximum)
    print("The lowest score is", minimum)
    
    
def main():
    filename = "scores.txt"
    
    if os.path.isfile(filename):
        scores = read_file(filename)
        maximum = calculate_max(scores)
        minimum = calculate_minimum(scores)
        average = calculate_average(scores)
        display_results(maximum, minimum, average)
    else:
        print("Need scores.txt to run program")
        

main()
