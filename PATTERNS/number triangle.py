n=int(input(""))
for i in range(1,n):
    s=1
    for j in range(n,0,-1):
        if j>i:
            print(" ",end='')
        else:
            print(s,end='')
            s+=1
    print()


