H=int(input("Enter Hour in 12 Hour format Number: "))
if(H>11 or H<1):
    print("INVALID INPUT!")
    exit(0)
M=int(input("Enter Minute Number: "))
if(M>60 or M<0):
    print("INVALID INPUT!")
    exit(0)
S=int(input("Enter Second Number: "))
if(S>60 or S<0):
    print("INVALID INPUT!")
    exit(0)

angleH=H*30
angleM=M/2
angleS=S/120

angleTotal=angleH+angleM+angleS

print(f"Hour Hand is at {angleTotal} from 12 o'clock")