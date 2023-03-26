n=int(input("enter a number to find factorial="))
fact=1
# for i in range(1,n+1,1):
#     fact*=i
# print(fact)
while(n>=1):
    fact*=n
    n-=1
print(fact)