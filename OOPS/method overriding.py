class Iphone3:
    def camera(self):
        print("camer is 8mpx")
class Iphone4(Iphone3):
    def camera(self):
        print("camera is 16mpx")
    def charging(self):
        print("fast charging")
i6=Iphone4()
i6.camera()
i6.charging()