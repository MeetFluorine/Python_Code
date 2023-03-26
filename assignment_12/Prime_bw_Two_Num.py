x=int(input("enter start of range:-"))
y=int(input("enter end of the range:-"))
for p in range(x,y+1,1):
    for i in range(2,p,1):
        if p%i==0:
            break
    else:
        print(p,end=' ')