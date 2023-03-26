def SquareNatural(n):
    x=1
    while n:
        yield x
        x+=1
        n-=1
for e in SquareNatural(int(input("enter a last number:-"))):
    print(e**2,end=' ')