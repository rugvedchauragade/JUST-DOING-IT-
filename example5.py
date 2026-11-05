# HYPOTENUSE OF A RIGHT ANGLED TRIANGLE
import math 
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
hypo = math.sqrt(pow(side1, 2) + pow(side2, 2))
print(f"The length of the hypotenuse is: {hypo}")