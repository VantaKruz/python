num=int(input("Enter a number: "))
sum=0
while(num!=0):
    temp=num%10
    sum+=temp
    num//=10
print(f"Sum of all digits is:{sum}")