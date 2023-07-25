class computer:
    def __init__(self,brand,cpu,ram,hdd) -> None:
        self.brand=brand
        self.cpu=cpu
        self.ram=ram
        self.hdd=hdd
    def showConfig(self):
        print("brand=",self.brand)
        print("cpu=",self.cpu)
        print("ram=",self.ram)
        print("hdd=",self.hdd)

print("enter first computer detail:-")
computer1= computer(input("brand:-"),input("cpu:-"),input("ram:-"),input("hard-disk:-"))
print("enter second computer detail:-")
computer2= computer(input("brand:-"),input("cpu:-"),input("ram:-"),input("hard-disk:-"))
print("enter third computer detail:-")
computer3= computer(input("brand:-"),input("cpu:-"),input("ram:-"),input("hard-disk:-"))
print("enter fourth computer detail:-")
computer4= computer(input("brand:-"),input("cpu:-"),input("ram:-"),input("hard-disk:-"))
print("\n\ncomputer 1 detail:-")
computer1.showConfig()
print("\n\ncomputer 2 detail:-")
computer2.showConfig()
print("\n\ncomputer 3 detail:-")
computer3.showConfig()
print("\n\ncomputer 4 detail:-")
computer4.showConfig()