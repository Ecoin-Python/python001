stds = []
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
    