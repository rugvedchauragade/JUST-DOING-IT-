#TEMPERATURE CONVERTER
unit = input("enter the unit (C/F):")
temp = float(input("enter the temperature:"))

if unit == "C":
    temp = (temp * 9/5) + 32
    print(f"the temperature is {temp} F")

elif unit == "F":
    temp = (temp - 32) * 5/9
    print(f"the temperature is {temp} C")

else : 
    print("invalid unit")