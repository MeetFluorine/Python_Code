def Natural(n):
    if n>1:
        Natural(n-1)
    print(n)

n=int(input("enter last number:-"))
Natural(n)