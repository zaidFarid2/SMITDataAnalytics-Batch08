class Student():
    def __init__(self,name,roll_No,portal_pass):
        self.name = name
        self.roll_No = roll_No
        self.__pas = portal_pass
        
    
    def display(self):
        return f"""student name is {self.name}

        rollNumber is {self.roll_No}"""
    
    def get_pass(self):
        return self.__pas


    def set_pass(self,new_pass): 
        self.__pas = new_pass
        return f"new pass is {self.__pas} "


s1 = Student("zaid","22fai109","!2222")

print(s1.get_pass())
print(s1.set_pass("123"))