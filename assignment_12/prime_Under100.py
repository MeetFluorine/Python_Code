for p in range(1,100,1):
    for i in range(2,p,1):
        if p%i==0:
            break
    else:
        print(p,end=' ')