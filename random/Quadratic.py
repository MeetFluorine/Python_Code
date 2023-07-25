print("standard form is ax^2+bx+c=0")
a=int(input("enter the value of a:-"))
b=int(input("enter the value of b:-"))
c=int(input("enter the value of c:-"))
d= (b**2)-(4*a*c)
if(d is 0):
    print("roots are real and equal")
elif(d>0):
    print("roots are real and distinct")
else:
    print("roots imaginary")
