def gen_Odd(n):
    x=1
    while n:
        yield x
        x+=2
        n-=1
for e in gen_Odd(int(input("enter a last number:-"))):
    print(e,end=' ')