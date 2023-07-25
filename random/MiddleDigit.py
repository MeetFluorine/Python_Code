num=int(input("enter a three digit number:-"))
x=num
last=num%10
num=num//10
middle=num%10
first= num//100
print("middle digit of %d is %d"%(x,middle))