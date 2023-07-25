class Greet:
    def __init__(self,name) -> None:
        self.name=name
    def show(self):
        print("Good Morning Mr. " +self.name)
    
user1= Greet(input("enter a name:-"))
user1.show()