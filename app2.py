

numbers = [10,20,40,50]

#print(numbers)

""" for x in numbers:
    print(x) """
    
str = "Welcom to Ecoin"

""" for s in str:
    print(s) """
    
    
""" for i in 100,200,300:
    print(i * 2)
 """
 
""" for i in range(1, 11):
    print(i) """
 
""" for i in range(1, 11):  # i<11  1 2 3
    print(i ** 2) """
 
""" x = 25
#x = x + 10
x += 10
x = x - 5 """

#print(x)
#sum_even  = 0
#2 + 4 + 6 + 8 + 10 ....20
#0 + 2 + 4 + 6
""" for i in range(2, 21, 2):
    sum_even += i
    
print("Sum of even numbers : ", sum_even) """

""" for i in range(10 , 0, -1):
    print(i) """
    
""" i  = 1
while i <= 10:
    print(i)
    i += 1 """
    
""" i = 1 
while i <= 10:
    print(i ** 2)
    i += 1 """


""" sum_even  = 0
i = 2
while i <= 20:
    sum_even += i
    i += 2

print("Sum of even numbers : ", sum_even) """

""" i = 10
while i >= 1:
    print(i)
    i -= 1 """
    
    
# Factorial   5! ===> 1 * 2 * 3 * 4 * 5

#  n! ===> 1 *2*2  *n


n = input("enter you number")
n = int(n)
#print( type(int(n)))
fac = 1
#fac = fac * i
for i in range(1, n + 1):
    fac *= i
    
print("Factorial of ",n," is ", fac) 




