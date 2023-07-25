class user:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age= age
    def __str__(self) -> str:
        return f"{self.name}({self.age})"
    
print("enter first user detail:-")
user1=user(input("enter name:-"),int(input("enter age:-")))
print("enter second user detail:-")
user2=user(input("enter name:-"),int(input("enter age:-")))
del user1.age
print("user1=",user1)
print("user2=",user2)
