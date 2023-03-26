def gen_Even(n):
    x=2
    while n:
        yield x
        x+=2
        n-=1
for e in gen_Even(int(input("enter a last number:-"))):
    print(e,end=' ')