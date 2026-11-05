#validate user input
# 1 ) username is no more than 12 characters 
#2. username must not contain any spaces 
# 3 username musst not contain any digits 

username = input ("ENTER YOUR USERNAME :")


if len(username) > 12 :
    print("your username cant be greater than 12 characters")

elif not username.find(" ") == -1:
    print("Your username cant contain spaces ")

elif not username.isalpha() :
    print("your username cant contain digits ")

else :
    print (f"welcome {username}")

