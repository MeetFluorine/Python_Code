def f1(l):
    
    return max(l)
l=list(map(int,input("enter some data with space separated:-").split(' ')))
max=f1(l)
l= len(l)
print(" maximum in %d numbers is :-%d"%(l,max))
