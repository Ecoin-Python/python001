# local scope
# global Scope
# keyword global

""" def myfunc():
    name = "Ali"
    print(name)
    
myfunc() """

#print(name)
""" myname = "imen"
def myfunc2():
    myname = "Ecoin"
    print(myname)
    
myfunc2()
print(myname) """

def myfunc3():
    global myname2
    myname2 = "Ali"
    print(myname2)
    

myfunc3()
print(myname2)
