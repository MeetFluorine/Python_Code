age=int(input("enter an age:-"))
match age:
    case age if(age>=60):
        print("senior citizen")
    case age if (40<=age<60):
        print("experienced")
    case age if(20<=age<40):
        print("young")
    case age if(10<=age<20):
        print("teen")
    case _:
        print("kid")