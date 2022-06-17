class Iphone5:
    def camera(self):
        print("camera iss 8mpx")
class Iphone6(Iphone5):
    def camera(self):
        print("camera is 16mpx")
        super(Iphone6,self).camera
    def charging(self):
        print("fast charging")
i8=Iphone6()
i8.camera()
i8.charging()