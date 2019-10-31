#Sum/Average Program
#Your first and last name: Arielle Sinicin
#Your student ID: s1222609

#Build on what you did in the 'List of Names' program
#Instead of entering 10 names, enter 20 numbers
#Instead of searching for a name in the list
#   Compute the sum of all 10 numbers
#   Compute the average for all 10 numbers

#Enter a number:
#The sum of the numbers you entered is:
#The average of the numbers you entered is:

numList = []
sumNum = 0
avgNum = 0.0

for i in range(0, 20): 
    num = int(input("Enter an integer: ")) 
    numList.append(num)
    sumNum += numList[i]

avgNum = sumNum/len(numList) 

print("The sum of the numbers you entered is:", sumNum)
print("The sum of the numbers you entered is:", avgNum)

#print("The sum of the numbers you entered is:", sum(numList) )
#print("The average of the numbers you entered is:", sum(numList)/len(numList) )
