year = int(input("Enter Year to check: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Year is Leap Year")
else:
    print("Year is not Leap Year")