class demo:
    name="abc2"
    def read(self):
        print("instance method")
    @classmethod
    def display(cls):
        print("class method name=",cls.name)
    @staticmethod
    def show():
        print("static method")
d=demo()
d.read()
demo.show()
demo.display()

                  
    