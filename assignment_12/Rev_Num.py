num=int(input("enter a number:-"))
x=num
rev=0
while(num!=0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
print("reverse of %d is %d"%(x,rev))