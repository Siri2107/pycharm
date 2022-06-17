import os,sys
fname=input("enter the filename :")
if os.path.isfile(fname):
    print("file is present")
    print("content  persent in file")
    print("----------------")
    f=open(fname,"r")
    data=f.read()
    print(data)
    f.close()
else:
    print("file is not present")
sys.exit(0)