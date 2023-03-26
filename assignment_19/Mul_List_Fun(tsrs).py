def f1(l):
    mul=1
    for e in l:
        mul*=e
    return mul
l=list(map(int,input("enter some data with space separated:-").split()))
mul=f1(l)
l= len(l)
print(" multiply of %d numbers is :-%d"%(l,mul))
