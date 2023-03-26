l1=[]
num=int(input("enter how much number you want:-"))
i=0
print("enter the number:-")
while(i<num):
    l1.append(int(input()))
    i+=1
print("sum of all element of list is %d"%(sum(l1)))