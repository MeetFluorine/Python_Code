def f1(x):
    l1= []
    for i in range(1, len(x)):
        l1.append(i**2)
    return l1
S= f1(range(1,30))
print(S)