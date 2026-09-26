X1=int(input("Enter X Coordinate of 1st Vertex: "))
Y1=int(input("Enter Y Coordinate of 1st Vertex: "))
X2=int(input("Enter X Coordinate of 2nd Vertex: "))
Y2=int(input("Enter Y Coordinate of 2nd Vertex: "))
X3=int(input("Enter X Coordinate of 3rd Vertex: "))
Y3=int(input("Enter Y Coordinate of 3rd Vertex: "))

if(X1==X2):
    X4=X3
elif(X1==X3):
    X4=X2
else:
    print("INVALID INPUT!")
    exit(0)
if(Y1==Y2):
    Y4=Y3
elif(Y1==Y3):
    Y4=Y2
else:
    print("INVALID INPUT")
    exit(0)
print(f"4th Vertex Coordinates: ({X4},{Y4})")