import csv 
with open("course.csv","a",newline="") as f:
    w=csv.writer(f)
    # w.writerow(["course name","fees","duaration"])
    # w.writerow(["python","6000","40"])
    # print("csv file created and data added")


    for i in range(3):
        course=input("enter the course name")
        fees=int(input("enter the course fees"))
        duaration=input("enter the  duaration")
        w.writerow([course,fees,duaration])
    print("data added to the course.csv")