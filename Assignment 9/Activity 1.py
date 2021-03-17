def calculateaverage(totalscore, count):
    amount = totalscore / count
    
    return amount

def calculatescore():
    count = 0
    totalscore = 0
    while True:    #This simulates a Do Loop
        count = count + 1
        score = getscore()
        totalscore = totalscore + score
        if not(score >= 0): break   #Exit loop
        amount = calculateaverage(totalscore, count)
    
    return amount

def displayscore(amount):
    print("Your average for entered scores is " + str(amount))

def getscore():
    print("Enter your score, if done then enter a negative score.")
    score = int(input())
    
    return score

# Main
# This program will ask for grade scores repeatedly until you enter a negative value, and then it will calculate and display the average for the entered scores.
amount = calculatescore()
displayscore(amount)
