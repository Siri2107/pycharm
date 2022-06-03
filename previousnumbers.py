previous_num=0
n=int(input("enter the range"))
for i in range(0,n):
    sum=i+previous_num
    print("current number is",i,"previous number is",previous_num,"sum:",sum)
    previous_num=i
