a=int(input("Enter first number: "))
operator=input("Select the operator(+,-,*,/): ")
b=int(input("Enter second number: "))

if(operator == "+"):
    print("Sum of the numbers is:",a+b)
elif(operator == "-"):
    print("Subtarction of number is:",a-b)    
elif(operator == "*"):
    print("Multiplication of the number is:",a*b)    
elif(operator == "/"):
    if(b != 0):
        print("Division of a by b is:",a/b)
    else:
        print("Not Divisibal by 0")
else:
    print("Invalid choice")
