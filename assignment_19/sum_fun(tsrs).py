def f1(l):
    
    return sum(l)
l=list(map(int,input("enter some data with space separated:-").split()))
sum=f1(l)
l= len(l)
print(" sum of %d numbers is :-%d"%(l,sum))
