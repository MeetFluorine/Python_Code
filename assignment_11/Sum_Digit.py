n=int(input("enter a number:-"))
sum=0
while(n>=1):
    sum+=(n%10)
    n=n//10
print(sum)
