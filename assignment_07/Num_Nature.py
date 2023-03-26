num=int(input("enter a number:-"))
match num:
    case num if num>0:
        print("%d is a positive number"%(num))
    case num if num<0:
        print("%d is a negative number"%(num))
    case _:
        print("%d is a zero"%(num))