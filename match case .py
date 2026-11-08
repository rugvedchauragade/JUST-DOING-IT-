# match case statement (switch) : an alternative to using many 'elif' statments 
#   execute some code if a value matches a 'case' 
#   benefits :cleaner and syntax is more readable 
def day_of_week(day):
    match day :
        case 1:
            return "it is monday"
        case 2 :
            return " it is tuesday"
        case 3 :
            return " it is wednesday"
        case 4 :
            return " it is thursday "
        case 5:
            return "it is friday "
        case 6:
            return " it is saturday "
        case 7:
            return " it is sunday "
        case _ :
            return "not a valid day "

print (day_of_week(1))
## we could also change the case name it doent have to no.
## case "monday" :
# u could also do case 1 | 2 | 3 : counts as 3 cases in one if we want same resut for threee cases 
