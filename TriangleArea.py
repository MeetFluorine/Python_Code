a=eval(input("enter the value of a:-"))
b=eval(input("enter the value of b:-"))
c=eval(input("enter the value of c:-"))
s=(a+b+c)/2
import math
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("area of a triangle of side(%d,%d,%d) is %.2f"%(a,b,c,area))
