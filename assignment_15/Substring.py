s1,s2=input("enter string:-"),input("enter substring:-")
if s2 in s1:
    print("yes, %s  is a substring of %s "%(s2,s1))
else:
    print("No, %s  is a substring of %s "%(s2,s1))