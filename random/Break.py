i=1
while(i<=3):
    x=int(input("enter an even number:-"))
    if(x%2==0):
        print("game won")
        break
    i+=1
if(i==4):
    print("game over")