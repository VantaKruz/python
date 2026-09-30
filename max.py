num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))

if(num1>num2):
    print(f"{num1} is greater")
elif(num2>num1):
    print(f"{num2} is greater")
else:
    print("Both numbers are equal")