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

mySum3(25,36,9,8,7,1)


def greet(*args):
    for name in args:
        print("Hello ",name)

names = ["Ali","Mahmoud","zineb","Imen","Khaled"]
greet(*names)


def multiply(*args):
    r = 1
    for num in args:
        r *= num
    print(r)
    
t = (25,36,9,8,7,1)    
multiply(*t)
