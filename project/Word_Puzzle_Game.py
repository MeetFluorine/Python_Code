def GenerateWord(s1):
    import random
    x=str(random.choice(s1))
    print(x)

    


name= input("enter your name:-")
print("Good Luck",name)
ans=input("Are you ready to play the game(y/n):-")
s1= ["fly","program", "hello"]
if ans=='y' or ans=='Y':
    GenerateWord(s1)
else:
    pass