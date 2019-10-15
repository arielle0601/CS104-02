
nameList = [] 
   
for i in range(0, 10): 
    name = str(input("Enter a name: ")) 
    nameList.append(name) # adding the element 
      
print(nameList) 

end = False

while end == False:
    search = input("Enter a name to search for or 'end' to stop the program: ")
    if search in nameList:
        print(search, "was found")
        
    elif search == "end":
        end = True
        
    else:
        print (search, "was not found")

print ("The program has ended")
