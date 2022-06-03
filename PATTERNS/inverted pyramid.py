n=int(input(""))
s=0
for i in range(n,0,-1):#revrse for loop
    s+=1
    for j in range(1,i+1):
        print(s,end="")
    print()
# n=int(input(""))
# for i in range(n,0,-1):
#     print(i,end='')