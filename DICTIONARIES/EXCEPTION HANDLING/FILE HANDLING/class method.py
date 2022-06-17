class Animal:
    legs=4
    @classmethod
    def walk(cls,name):
        print("{} walks with {} legs...".format(name,cls.dogs))
Animal.walk("dog")
Animal.walk("cat")        


