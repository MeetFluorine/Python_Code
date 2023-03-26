n=int(input("enter a limit:-"))
sum=0
# print(sum(range(n+1)))
for i in range(1,n+1,1):
    sum+=i**2
print(sum)