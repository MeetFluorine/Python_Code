def PrintEven(l1):
    for i in l1:
        if i%2==0:
            print(i,end=' ')
            


l1= list(map(int, input("enter some data :-").split()))
PrintEven(l1)