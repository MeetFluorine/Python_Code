year=int(input("enter a year:-"))
match year:
    case year if year%100==0 and year%400==0 and year%4==0:
        print("%d is a century leap year"%(year))
    case year if year%100!=0 and year%400==0 and year%4==0:
        print("%d is a Non century leap year"%(year))
    case year if year%100==0 and year%400!=0 and year%4!=0:
        print("%d is a century leap year"%(year)) 
        # need modification