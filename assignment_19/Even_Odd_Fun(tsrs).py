def Even(a):
    if(a%2==0):
        return "even"
    else:
        return "odd"
a= int(input("enter a number:-"))
print("%d is an/a"%(a),Even(a))