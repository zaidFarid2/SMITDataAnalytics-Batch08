class User():
    
    def __init__(self,name,password):
        self.name = name
        self.password = password
        self.login_attemp = 0

    def inc(self):
        if(self.name == "zaid" and self.password == "123"):
            self.login_attemp+=1
            print(f"login attemp is {self.login_attemp}")

    # def dec(self):
        
    #     self.login_attemp-=1
    #     print(f"login attemp is {self.login_attemp}")

    def reset(self):
        self.login_attemp = 0
        print(f"login attemp is {self.login_attemp}")



attemp1 = User("zaid","123")
attemp1.inc()
attemp1.inc()
attemp1.reset()

