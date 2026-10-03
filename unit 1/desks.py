aStudents=int(input("Enter Students in class A: "))
if(aStudents%2!=0):
    aStudents+=1
bStudents=int(input("Enter Students in class B: "))
if(bStudents%2!=0):
    bStudents+=1
cStudents=int(input("Enter Students in class C: "))
if(cStudents%2!=0):
    cStudents+=1
aDesks=aStudents/2
bDesks=bStudents/2
cDesks=cStudents/2

print(f"Desks required for A class: {aDesks} \nDesks required for B class: {bDesks} \nDesks required for C class: {cDesks}")
print("Total Desks needed: ", aDesks+bDesks+cDesks)