class User():
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.__password = password
        self.login_attemp = 0
        User.inc_login_attemp(self)
    def inc_login_attemp(self):
        self.login_attemp += 1
        print(f"object created: {self.login_attemp}")
    
    def __del__(self):
        User.dec_login_attemp(self)

    def dec_login_attemp(self):
        self.login_attemp -= 1
        print(f"object decreased: {self.login_attemp}")

p1 = User("zaid","zaid@",123)
p2 = User("zaid","zaid1",55)
p2.inc_login_attemp()


        




    # def res_login_attemp()