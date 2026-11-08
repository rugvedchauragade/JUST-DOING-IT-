#LOGICAL OPEARTORS
# or = at leat one condition must be true
# and = all conditions must be true
# not = reverses the result, returns False if the result is true

temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining :
    print(" the outdoor event is cancelled")

else :
    print("the outdoor is going to be held ")


temp = 30  # temp is now this one  not from above 
is_sunny = False 
if temp >= 28  and is_sunny :
    print ("it is hot outside ")
    print (" it is sunny 😊")

elif temp <= 0 and is_sunny :
    print (" it is cold outside ")
    print (" it is sunny")

elif temp < 28 and temp > 0 and is_sunny :
    print(" it is warm outside 🥵")
    print(" it is sunny🌞")

elif temp >= 28 and not is_sunny: # inverts false to true , true to false 
    print("it is hot outside")
    print (" it is cloudy☁️")

