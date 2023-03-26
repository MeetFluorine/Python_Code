a,b=int(input("enter first number:-")),int(input("enter second number:-"))
flag=0
max=a if a>b else b
while(flag!=1):
    if(max%a==0 and max%b==0):
        print("LCM of %d and %d is %d"%(a,b,max))
        flag=1
    else:
        max+=1