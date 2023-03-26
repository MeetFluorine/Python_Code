num= int(input("enter a number:-"))
match num:
    case num if num%2==0:
        print("Saurabh Shukla")
    case num if num<0 and num%2:
        print("Prateek Jain")
    case num if num>0 and num%2:
        print("aditya chopra")