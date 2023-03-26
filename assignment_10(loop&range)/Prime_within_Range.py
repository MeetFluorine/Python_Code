for p in range(15,45,1):
    for i in range(2,p,1):
        if p%i==0:
            break
    else:
        print(p,end=' ')