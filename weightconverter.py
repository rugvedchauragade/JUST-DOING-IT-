# WEIGHT CONVERTER 
weight = float(input("Enter weight  : "))
unit = input("Enter unit (kg, lb): ")
if unit == "kg":
    weight = weight * 2.20462
    unit = "lb"
    print(f"Weight in {unit}: {weight:.2f}")

elif unit == "lb":
    weight = weight / 2.20462
    unit = "kg"
    print(f"Weight in {unit}: {weight:.2f}")
  
else:
    print("Invalid unit. Please enter 'kg' or 'lb'.") 
  
