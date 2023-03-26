def PrimeNumber(n):
    N=n*2
    x=1
    while N:
        yield x
        x+=1
        N-=1
for e in PrimeNumber(int(input("enter a last number:-"))):
    for i in range(2,e):
        if e%i==0:
            break
    else:
        print(e)