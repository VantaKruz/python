num=int(input("Enter a number: "))

while (num!=0):
    temp=num%10
    print(int(temp), end='')
    num=num//10
print("")