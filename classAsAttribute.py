#class as attribute


class Depart_Course:
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = self.compulsory_course("eng","urdu","isl")
    def show(self):
        print(self.m1,self.m2,self.m3)
        self.m4.show()


    class compulsory_course:
        def __init__(self,s1,s2,s3):
            self.s1 =s1
            self.s2 =s2
            self.s3 =s3
        def show(self):
            print(self.s1,self.s2,self.s3)


s1 = Depart_Course("ai","ml","networking")
s1.show()