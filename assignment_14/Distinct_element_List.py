l1=[]
l2=[]
num=int(input("enter how much number you want:-"))
i=0
print("enter the number:-")
while(i<num):
    l1.append(eval(input()))
    i+=1
for e in l1:
    if(l1.count(e)==1):
        l2.append(e)
print(l2)