# from abc import ABC,abstractmethod
# class parent(ABC):
#     def common(self):
#         print("parent")
#     @abstractmethod
#     def vary(self):
#         pass 
# class child(parent):
#         def vary(self):
#             print("child")
# obj=child()
# obj.common()
# obj.vary()


##a method having only decleration but no implimentation
# from abc import *
# class Method:
#     @abstractmethod
#     def sum(self):
#         pass
#     def display(self):
#         print("display method")
# m=Method()
# m.display()


##any class having at least one abstract method = abstract class
# from abc import*
# class Iphone(ABC):#abstract class
#     def camera(self):
#         pass

# class Iphone1(Iphone):
#     def camera(self):
#         print("camera is 8mpx")
# obj=Iphone1()
# obj.camera()


##class containing all method as abstract method =interface
from abc import *
class Srav(ABC):
    @abstractmethod
    def student(self):
        pass
    @abstractmethod
    def student2(self):
        pass
class Siri(Srav):
    def student(self):
        print("good")
    def student2(self):
        print('bad')
obj=Siri()
obj.student()
obj.student2()





