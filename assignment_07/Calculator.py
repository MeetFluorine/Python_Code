print("press 1 for Addition\npress 2 for Subtraction\npress 3 for Multiplication\npress 4 for division")
op=int(input("enter your choice here:-"))
match(op):
    case 1:
        x=int(input("enter 1st number:-"))
        y=int(input("enter 2nd number:-"))
        print("sum of %d and %d is %d"%(x,y,x+y))
    case 2:
        x=int(input("enter 1st number:-"))
        y=int(input("enter 2nd number:-"))
        print("sub of %d and %d is %d"%(x,y,x-y))
    case 3:
        x=int(input("enter 1st number:-"))
        y=int(input("enter 2nd number:-"))
        print("mul of %d and %d is %d"%(x,y,x*y))
    case 4:
        x=int(input("enter 1st number:-"))
        y=int(input("enter 2nd number:-"))
        print("div of %d and %d is %.2f"%(x,y,x/y))