#Python Richter Scale Calculation
#Your first and last name: Arielle Sinicin
#Your ID: s1222609

#Algorithm:
# ask the user to 'Enter the Richter scale value: '
#   hint1: use an 'input' statement to input a variable called 'richter'
#   hint2: make sure 'richter' is a 'floating point' by using 'float'
# make sure richter scale value is greater than 0
#   if not, print "Value must be greater than 0"
# determine the Effect for the Richter scale value entered
#   hint1: use 'if' 'elif' and 'else' statements
#   hint2: remember to use ':' following all 'if' 'elif' and 'else' statements
# display or print the Effect
#   hint: use 'print' statement (only 1 effect should print)
# ask the user if they want to enter another value

# test your program several times with the following values:
#   8.1, 8.0, 7.1, 7.0, 6.1, 6.0, 4.6, 4.5, 4,4, -4.6

over = False

while over != True:
    richter = float(input("Enter the Richter scale value: "))
    if richter >= 8.0:
        print("Most structures fall") 
    elif richter >= 7.0:
        print("Many buildings destroyed")  
    elif richter >= 6.0:
        print("Many buildings considerably damaged, some collapse")  
    elif richter >= 4.5:
        print("Damage to poorly constructed buildings")
    elif richter >= 0:
        print("No destruction of buildings")
    elif richter < 0.0:
        print ("Value must be greater than 0")
    else:
        print ("")
    again = str(input("Would you like to enter another value? Enter yes or no: "))
    if again == "yes":
        over = False
    else:
        over = True


