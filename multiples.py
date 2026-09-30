num=int(input("Enter a number: "))

print(f"Multiples of {num} are:")
for x in range(num+1):
    if(x!=0):
        if(num%x==0):
            print(x)
