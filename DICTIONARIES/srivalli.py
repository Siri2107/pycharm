from xml.dom.pulldom import CHARACTERS


f=open("srivalli.txt","w")

f.write("hii we are from python7pm batch\n")
f.write("hey siri\n")
f.write("hii sravani\n")
f.write("heelo world\n")

f.close()



f=open("srivalli.txt","r")
# data=f.readlines()
# print(data)
# count=len(data)
# print(count)
lines=0
char=0
for line in f:
    line=line.strip("\n")
    char+=len(line)
    lines+=1
    print(line)
print(char)
print(lines)

f.close()



