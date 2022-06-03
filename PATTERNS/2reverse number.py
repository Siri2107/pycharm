# n=int(input(""))
# for i in range(0,n+1):
#     for j in range(n-i,0,-1):
#         print(j,end="")

#     print()

n=int(input(""))
for i in range(n+1):
    for j in range(i):
        print(j,end="")
    print()