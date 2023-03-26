def NaturalRev(n):
    if n>=1:
        print(n)
        NaturalRev(n-1)

n=int(input("enter last number:-"))
NaturalRev(n)