l1=[]
num=int(input("enter how much number you want:-"))
i=0
print("enter the number:-")
while(i<num):
    l1.append(int(input()))
    i+=1
print("%d is minimum among all"%(min(l1)))