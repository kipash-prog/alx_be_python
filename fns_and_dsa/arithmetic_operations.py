def perform_operation(num1,num2,operation):
    if operation=="add":
       return num2+num1
    if operation=="subtract":
       return num2+num1
    if operation=="multiply":
       return num1*num2
    if operation=="divide":
        if(num2 !=0):
          return num1/num2
        else:
           print("can't divided zero.")
        


