day=int(input("Enter Day of Month: "))
if(day>32 or day<1):
    print("INVALID DATE!")
    exit(0)
month=int(input("Enter Number of Month: "))
if(month>12 or month<1):
    print("INVALID DATE!")
    exit(0)
yr=int(input("Enter year: "))

if(month%2==0 and month!=2):
    if(day<31):
        print("Date is Valid")
    else:
        print("Date is Invalid")
elif(month%2!=0):
    if(day<32):
        print("Date is Valid")
    else:
        print("Date is Invalid")
if(month==2):
    if(day<29 and yr%4!=0):
        print("Date is Valid")
    elif(yr%4==0 and day<30):
        print("Date is Valid")
    else:
        print("Date is Invalid")