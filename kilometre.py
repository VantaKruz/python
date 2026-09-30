print("Enter 1 to convert miles to kilometres")
ch=int(input("Enter 2 to convert kilometres to miles"))
mil=0
kilo=0
match ch:
    case 1:
      mil=int(input("Enter Distance in miles: "))
      kilo=1.61*mil
      print(f"Distance in Kilomtres:{kilo}")
    case 2:
      kilo=int(input("Enter Distance in kilometres: "))
      mil=0.62*kilo
      print(f"Distance in Miles:{mil}")