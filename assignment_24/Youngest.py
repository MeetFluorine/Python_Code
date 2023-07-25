class user:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age= age
    
print("enter first user detail:-")
user1=user(input("enter name:-"),int(input("enter age:-")))
print("enter second user detail:-")
user2=user(input("enter name:-"),int(input("enter age:-")))
print("enter third user detail:-")
user3=user(input("enter name:-"),int(input("enter age:-")))
(print("%s is youngest(%d) among all"%(user1.name,user1.age)) if user1.age<user3.age else print("%s is youngest(%d) among all"%(user3.name,user3.age))) if user1.age<user2.age else(print("%s is youngest(%d) among all"%(user2.name,user2.age)) if user2.age<user3.age else print("%s is youngest(%d) among all"%(user3.name,user3.age)))
