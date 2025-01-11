class Student():
    University = "Duet" ###class variable 
    uniFullName = "dawood university of Enigineering"
    def __init__(self,name,depart):
        self.name = name
        self.depart = depart
    
    def show(self):
        return f" name is {self.name} and depatment is {self.depart} "
    
    @classmethod
    def Uni_info(self):
        return f"university name is {self.uniFullName} "

    @staticmethod
    def std_info():
        return f"Student is graduated from xyz Uni"



s1 = Student("Zaid","ai")
s2 = Student("ibad","ai")

print(s1.std_info())    ### does'nt required any arguiment 

# print(Student.Uni_info()) its require arguement like class or
# print(s1.Uni_info())

# print(s1.show())
# print(Student.show(s1))

# print(Student.University)


# print(s1.University)
# print(s2.University)