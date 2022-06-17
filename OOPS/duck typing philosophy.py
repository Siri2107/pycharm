class Men:
    def talk(self):
        print("men are talking")
class Women:
    def talk(self):
        print("women are talking")
class Children:
    def talk(self):
        print("children are talking")
l=[Men(),Women(),Children()]
for i in l:
    i.talk()
