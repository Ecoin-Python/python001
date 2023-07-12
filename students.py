# main 

# welcom to Ecoin
# 1 Add Student (fname,lname,age,year)  
# 2 list_Student()
# 3 Get_Student(num) 
# 4 Exit  ==> exit()
stds = []

#[["ahmed","kadri",25,2005],["ahmed","kadri",25,2005],["ahmed","kadri",25,2005]]
def addStudent(fname,lname,age,year):
    std = []
    std.append(fname)
    std.append(lname)
    std.append(age)
    std.append(year)
    stds.append(std)
    return stds
def listStudent():
    for std in stds:
        print(std)
def getStudent(num):
    print(stds[num])
    
    
    
def main():
    print("welcom to Ecoin ")
    print("1 Add Student ")
    print("2 list Student ")
    print("3 Get_Student ")
    print("4 Exit ")
    
    choice = int(input("Enter your Choice :"))
    if choice == 1:
        fname = input("Enter Your first Name :")
        lname = input("Enter Your Last Name :")
        age = int(input("Enter Your Age :"))
        year = int(input("Enter Year :"))
        addStudent(fname,lname,age,year)
        main()
    elif choice == 2:
        listStudent()
        main()
        
    elif choice == 3:
        num = int(input("Enter Student number : "))
        getStudent(num)
        main()
        
    elif choice == 4:
        exit()
    else:
        print("Invalid Choice ")
        main()
        

main()    
    