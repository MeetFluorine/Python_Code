def Min(a,b,c):
    return((a if a<c else c) if a<b else(b if b<c else c))


a,b,c= int(input("enter first number:-")),int(input("enter second number:-")),int(input("enter third number:-"))
x=Min(a,b,c)
print("%d is the smallest element"%(x))


# another way
# def Min(l1):
#     print(min(l1))
# l1= list(map(int,input("enter three number:-").split()))
# Min(l1)