from typing_extensions import Self


class Iphone3:
    def __init__(self):
        self.camera="none"
    
class Iphone4(Iphone3):
    def __init__(self):
        self.camera="null"

    def display(slef):
        print(self.camera)
    
i4=Iphone4()
i4.display()


# class parent:
#     def f(self):
#         print("the f method in parent class")
# class child(parent):
#     def f(self):
#         print("the f method in child class")
        
# ob1 = child()
# ob1.f()