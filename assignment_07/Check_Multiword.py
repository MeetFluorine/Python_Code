s= input("enter a string:-")
s.strip()
match s:
    case s if ' ' in s:
        print("Multi word string")
    case s if ' ' not in s:
        print("single word string")