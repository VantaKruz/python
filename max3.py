num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
num3=int(input("Enter 3rd number: "))

if(num1<num2 and num1<num3):
    if(num2>num3):
        print(f"{num2} is the greatest number")
    elif(num2<num3):
        print(f"{num3} is the greatest number")
    else:
        raise ValueError("Multiple Numbers are the same!")
elif(num2<num1 and num2<num3):
    if(num1>num3):
        print(f"{num1} is the greatest number")
    elif(num1<num3):
        print(f"{num3} is the greatest number")
    else:
        raise ValueError("Multiple Numbers are the same!")
elif(num3<num2 and num3<num1):
    if(num1>num2):
        print(f"{num1} is the greatest number")
    elif(num1<num2):
        print(f"{num2} is the greatest number")
    else:
        raise ValueError("Multiple Numbers are the same!")
else:
    raise ValueError("Multiple Numbers are the same!")