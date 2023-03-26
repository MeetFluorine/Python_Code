def Fibonacci(n):
    x,y=0,1
    while n:
        yield x
        x,y=y,x+y
        n-=1
for e in Fibonacci(int(input("enter a last number:-"))):
    print(e,end=' ')