def decor(name):
    def inner(name):
        if name=="siri":
            print("very very good morning")
     
        else:    
            return inner
        
        
def wish(name):
    print(name,"good morning")
wish("siri")