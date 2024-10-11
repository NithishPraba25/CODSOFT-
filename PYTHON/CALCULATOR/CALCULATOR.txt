while True:
    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the second number: "))
    print("Choose the operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    choice = input("Enter the number corresponding to the operations(1/2/3/4): ")
    if choice=='1':
        result=num1+num2
        print(f"The result of {num1}+{num2} is: {result}")
        
    elif choice == '2':
        result=num1-num2
        print(f"The result of {num1}-{num2} is: {result}")
    elif choice=='3':
        result=num1*num2
        print(f"The result of {num1}*{num2} is: {result}")
    elif choice=='4':
        if num2!=0:
            result=num1/num2
            print(f"The result of {num1}/{num2} is: {result}")
        else:
            print("Division by zero Error")
    else:
        print("Invalid operation choice")
        
    cont=input("Do you want to perform another calculation?(y/n): ").lower()
    print('\n')
    if cont!= 'y':
        print("THANK YOU FOR USING!")
        break
