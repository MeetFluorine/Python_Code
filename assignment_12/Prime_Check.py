num=int(input("enter a number:-"))
for i in range(2,num,1):
    if(num%i==0):
        print("%d is not a prime number"%(num))
        break
else:
    print("%d is a prime number"%(num))