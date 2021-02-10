# This program will convert miles into yards, feet, and inches

print("Enter # of miles")
miles = float(input())

yards = miles * 1760
feet = miles * 5280
inches = miles * 63360

print(" The total distance is ")
print(str(yards) + " yards, ")
print(str(feet) + " feet, and ")
print(str(inches) + " inches. ")
