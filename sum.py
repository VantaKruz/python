num=int(input("Enter the limit: "))

sum=0

for x in range(num+1):
    if(x!=0):
        sum+=x
final=sum/num
print(final)