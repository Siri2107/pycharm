class Iphone4:
    def camera(self):
        print("camera is 4mpx")
class Iphone5(Iphone4):
    def screen(self):
        print("screen is 5 inches")
i5=Iphone5()
i5.camera()
i5.screen()