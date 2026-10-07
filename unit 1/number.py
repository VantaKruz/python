n=int(input("Enter value of n: "))

n1=int(input("Enter card 1: "))
n2=int(input("Enter card 2: "))
n3=int(input("Enter card 3: "))
n4=int(input("Enter card 4: "))
total=n*(n+1)//2
lost=total-(n1+n2+n3+n4)

print(f"{lost} is the lost number")