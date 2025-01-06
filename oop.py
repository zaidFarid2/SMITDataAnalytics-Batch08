class Student():
    def __init__(self,name,rollNo,course):
        self.name = name 
        self.rollNo = rollNo 
        self.course = course 

    def display(self):
        return(f"name is {self.name} roll no is {self.rollNo} course is {self.course}")


p1 = Student("zaid",108,"ai")
print(p1.course)
print(p1.display())