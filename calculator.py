import time
while(True):
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print("Enter 1 for Addition")
    print("Enter 2 for Subtraction")
    print("Enter 3 for Multiplication")
    print("Enter 4 for Division")
    ch=int(input("Enter 5 to exit: "))

    match ch:
        case 1:
            print("Addition: ", a+b)
            print("Enter 1 to Return to main menu")
            chA=int(input("Enter 2 to exit: "))
            match chA:
                case 1:
                    continue
                case 2:
                    exit(0)
        case 2:
                    print("Subtractiom: ", a+b)
                    print("Enter 1 to Return to main menu")
                    chA=int(input("Enter 2 to exit: "))
                    match chA:
                        case 1:
                            continue
                        case 2:
                            exit(0)
        case 3:
                    print("Multiplication: ", a*b)
                    print("Enter 1 to Return to main menu")
                    chA=int(input("Enter 2 to exit: "))
                    match chA:
                        case 1:
                            continue
                        case 2:
                            exit(0)
        case 4:
                    print("Division: ", a/b)
                    print("Enter 1 to Return to main menu")
                    chA=int(input("Enter 2 to exit: "))
                    match chA:
                        case 1:
                            continue
                        case 2:
                            exit(0)
        case 5:
            print("exiting.....")
            time.sleep(2)
            exit(0)