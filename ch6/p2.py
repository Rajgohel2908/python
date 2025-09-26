m1 = int(input("Enter cpp marks:"))
m2 = int(input("Enter c marks:"))
m3 = int(input("Enter python marks:"))

tot_per = (m1+m2+m3)/3

print("percentage:",tot_per and m1 and m2 and m3 >=33)
if(tot_per>=40):
    print("student is pass")
else:
    print("Student is fail")