str="pynative"
print(str)
print("only even index characters:",str[0::2])

s=input("enter the string:")
print(len(s))
for i in range(0,len(s),2):
    print(s[i])
