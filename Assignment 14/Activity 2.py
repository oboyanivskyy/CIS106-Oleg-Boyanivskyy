# This program will copy a list of names and grade scores
# into a text file and then display high, low, and average
# scores.
import os
import sys


def read_file(filename):
    scores = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line == "Name,Score":
                pass
            else:
                numeric_filter = filter(str.isdigit, line)
                line = "".join(numeric_filter)
                scores.append(line)
    scores = list(map(int, scores))
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            print(line)
    print(scores)
    
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
    try:
        scores = read_file(filename)
        maximum = calculate_max(scores)
        minimum = calculate_minimum(scores)
        average = calculate_average(scores)
        display_results(maximum, minimum, average)
    except TypeError:
        print("Error: Missing or bad data")
    except ValueError:
        print("Error: Missing or bad data")
    except IndexError:
        print("File is empty")
    except FileNotFoundError:
        print("File is missing")
        

main()