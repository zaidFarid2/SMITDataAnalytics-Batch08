# class Car():
#     def __init__(self,model,name,color):
#         self.model = model
#         self.name = name
#         self.color = color

#     def display(self):
#         return(f"name of car and model is {self.name} {self.model} with {self.color} color")


# car1 = Car(2006,"BMW i5","black")
# print(car1.color)
# print(car1.model)
# print(car1.name)
# print(Car.display(car1))


class Std():
    def __init__(self,name,rollNo):
        self.name =name
        self.rollNo =rollNo
    def display(self):
        return f"naem is {self.name} and roll no is {self.rollNo}"


s1 =Std("zaid","22f-BSAI-109")
print(s1.display())