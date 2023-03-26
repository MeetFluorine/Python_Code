def PrimeNumber(n):
    x=1
    while n*2:
        yield x
        x+=1
        n-=1
for e in PrimeNumber(int(input("enter a last number:-"))):
    for i in range(2,e):
        if e%i==0:
            break
    else:
        print(e)