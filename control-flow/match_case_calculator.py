num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
operation=input("Choose the operation (+, -, *, /):")

match operation:
    case "+":
        result=int(num1 + num2) 
        print("The result is ",result,".")
    case "-":
        result = num1-num2
        print("The result is ",result,".")
        
    case "*":
        result = num1 * num2
        print("The result is ",result,".")
    case "/":
        if num2!=0:
            result=num1/num2
            print("The result is ",result,".")
        else:
            print("Cannot divide by zero.")

            

