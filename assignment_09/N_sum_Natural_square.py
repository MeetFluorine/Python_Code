n=int(input("enter a desire number:-"))
sum=0
i=1
print("number","square"," sum",sep="\t")
while i<=n:
    print(" ",i,end='\t')
    print(" ","%d"%(i**2),end="\t")
    sum+=i**2
    print(" ","%d"%(sum))
    i+=1    
print("sum of %d number is %d"%(n,sum))
