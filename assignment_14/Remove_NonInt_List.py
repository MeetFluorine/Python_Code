l1=[]
num=int(input("enter how much number you want:-"))
i=0
print("enter the number:-")
while(i<num):
    l1.append(eval(input()))
    i+=1
for e in l1:
    if(type(e)!=int):
        l1.remove(e)
print(l1)