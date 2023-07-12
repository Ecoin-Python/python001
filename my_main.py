import module_std as getionEtudiant

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
        getionEtudiant.addStudent(fname,lname,age,year)
        main()
    elif choice == 2:
        getionEtudiant.listStudent()
        main()
        
    elif choice == 3:
        num = int(input("Enter Student number : "))
        getionEtudiant.getStudent(num)
        main()
        
    elif choice == 4:
        exit()
    else:
        print("Invalid Choice ")
        main()
        

main()    
    