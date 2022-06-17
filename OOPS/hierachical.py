class Iphone1:
    def camera(self):
        print("12mpx camera")
class Iphone2(Iphone1):
    def display(self):
        print("led display")
class Iphone3(Iphone1):
    def battery(self):
        print("300mah")
i8=Iphone2()
i8.camera()
i8.display()

i9=Iphone3()
i9.battery()
i9.camera()
