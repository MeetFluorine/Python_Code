class user:
    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email= email
    # def get_info(self):
    #     self.name=input("enter name of the user:-")
    #     self.age=int(input("enter age of the user:-"))
    #     self.email=input("enter email:-")
    def show_info(self):
        print("name=",self.name,)
        print("age=",self.age)
        print("email=",self.email)
        
user1= user("chandan",20,"chandangee77@gmail.com")

# user1.get_info()
user1.show_info()