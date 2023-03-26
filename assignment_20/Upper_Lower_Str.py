def CountUpperLower(s1):
    upper=0
    lower=0
    for i in s1:
        if i.isupper():
            upper+=1
        if i.islower():
            lower+=1
    print(" %d upper and %d lower character present in %s "%(upper,lower,s1))


s1=input("enter a mix string:-")
CountUpperLower(s1)