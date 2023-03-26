x=int(input("enter a number:-"))
num=x
count=0
while(x!=0):
    count+=1
    x=x//10
print("no of digit in %d is %d"%(num,count))