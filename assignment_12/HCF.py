a,b=int(input("enter 1st number:-")),int(input("enter 2nd number:-"))
i=1
while(i<=a or i<=b):
    if(a%i==0 and b%i==0):
        hcf=i
    i+=1
print("HCF of %d and %d is %d"%(a,b,hcf))
