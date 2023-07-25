class school:
    college="SRGC MZN"
    def __init__(self,name,roll,sec) -> None:
        self.name=name
        self.roll=roll
        self.sec=sec
    # print(college)
    def show(self):
        print(school.college)
        print("Name=",self.name)
        print("Roll No.=",self.roll)
        print("section=",self.sec)


student1=school(input("enter name of student:-"),int(input("enter roll no.:-")),input("enter section:-"))
student1.show()