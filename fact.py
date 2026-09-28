num=int(input("Enter a number: "))
if num<1:
    raise ValueError("INVALID INPUT")
fact=1
for x in range(num+1):
    if(x!=0):
        fact*=x
print(f"Factorial of {num} is {fact}")