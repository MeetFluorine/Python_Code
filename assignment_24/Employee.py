class Employee:
    company="SRGC MZN"
    def __init__(self) -> None:
        self.empid=  int(input("enter employee id:-"))
        self.name=   input("enter employee name.:-")
        self.salary= int(input("enter salary:-"))
    # print(college)
    def show(self):
        print(Employee.company)
        print("employee id=",self.empid)
        print("Name.=",self.name)
        print("salary=",self.salary)


Employee1=Employee()
Employee1.show()