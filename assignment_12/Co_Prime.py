x=int(input("enter first number:-"))
y=int(input("enter second number:-"))
l1=[]
l2=[]
for i in range(2,x+1,1):
    if(x%i==0):
        l1.append(i)
for j in range(2,y+1,1):
    if(x%i==0):
        l2.append(i)
for k in l1:
    for l in l2:
        if(k==l):
            print("not a co prime")
            break
