""" def ssum(a,b):
    c = a + b
    print(c)
    
ssum(15,25)
ssum(20,25) """

#exo calc
#a b  op 
# op == '+'   a +b 
# op == '-'   a -b 
# op == '*'   a *b 
# op == '/'   a / b 

def calc(a, b, op):
    if(op=='+'):
        print(a + b)
    
    elif(op == '-'):
        print(a - b)
    elif(op == "*"):
        print(a * b)
    elif(op == "/"):
        if(b == 0):
            print("div By Zero")
        else:
            print(a / b)
    else:
        print("No operation")
        
#calc(25,10,'/')



def mySum(a,b):
    return a + b
    
def mySum2(a,b, c):
    return a + b + c
#res = mySum(10,2)
#print(res)

#print(mySum2(15,2,5))

def mySum3(*args):
    sum = 0
    for c in args:
        #sum = sum + c 
        sum += c
    print(sum)
        
#t = (25,36,9,8,7,1)

# mySum3(25,36,9,8,7,1)


def greet(*args):
    for name in args:
        print("Hello ",name)

names = ["Ali","Mahmoud","zineb","Imen","Khaled"]
#greet(*names)


def multiply(*args):
    r = 1
    for num in args:
        r *= num
    print(r)
    
t = (25,36,9,8,7,1)    
    
""" multiply(*t)
multiply(5,6,2)
multiply(25,3)
multiply(7,8,9,2,36) """



def listLang(**l):
    print(l.items())
    for lg,version in l.items():
        print(lg," ==== ",version)


lang = {"php":8.2,"python":3.9,"java":17,"kotlin":2.3}
listLang(**lang)


def order(**kwargs):
    total = 0
    it = " "
    print(kwargs.items())
    for item, price in kwargs.items():
        total += price
        
        
    print("my total Order is ",total)



myorder = {"laptop":45000,"mouse":450,"iphone":256655}  
order(**myorder)  


#format String 

fname = "Ali"
lname = "kadri"
age = 25


#print("My first Name is ",fname," and my Last Name is :",lname," and i am ",age," years old") 
#print("My first Name is {1}  and my Last Name is :{2} and i am {0} years old".format(age,fname,lname)) 
print("My first Name is {f_name}  and my Last Name is :{l_name} and i am {my_age} years old".format(my_age = age,f_name = fname,l_name = lname)) 