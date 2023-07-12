#print(1 + 1 == 3)  # logical Error 
""" def myfunc():
    name = "Ali"

deff myfun2():  # Logical error
    print("Ecoin")
    
        
print(name)  # logical Error """

# Exception Error
try:
    num1 = int(input("enter Number 1: "))
    num2 = int(input("enter Number 2: "))
    print(" the result = ",num1/num2)

except ZeroDivisionError:
    print("Div By Zero from Ecoin")

except:
    print("Error from Ecoin")
else:
    print("No Error") 
finally:
     print("End program from finally ")  
