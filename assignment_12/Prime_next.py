# not solved yet
num=int(input("enter a number:-"))
for p in range(num,num+200,1):
    for i in range(2,p,1):
        if(p%i==0):
            break
    else:
        print(i)