num=int(input("Enter a number: "))
prime=True
for x in range(num+1):
    if(x!=0 and x!=1 and x!=num):
        if(num%x==0):
            prime=False
if(prime):
    print("Number is Prime")
else:
    print("Number is not Prime")