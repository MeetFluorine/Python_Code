s1=input("enter 1st string:-")
s2= input("enter 2nd string:-")
match (s1,s2):
    case (s1,s2) if s1==s2:
        print("both are identical")
    case (s1,s2) if s1>s2:
        print("{} comes before {}",format(s1,s2))