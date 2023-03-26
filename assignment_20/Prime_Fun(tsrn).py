def Prime(n):
    for i in range(2,n,1):
        if(n%i==0):
            print("%d is not a prime number"%(n))
            break
        print("%d is a prime number"%(n))
        break

n= int(input("enter a number to check :-"))
Prime(n)
