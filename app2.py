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


""" n = input("enter you number")
n = int(n)
#print( type(int(n)))
fac = 1
#fac = fac * i
for i in range(1, n + 1):
    fac *= i
    
print("Factorial of ",n," is ", fac)  """


""" n = 6 
fact2 = 1
i = 1 
while i <= n:
    fact2 *= i
    i += 1
    
print("Factorial of ",n," is ", fact2)  """


""" str = "python"  #==> niocE oT mocleW
str_rev = ""
i = len(str) - 1
while i >= 0 :
    str_rev += str[i]
    i -= 1
    
print("Reverse Str ",str_rev)  """

 # Tuple Dict Set
 
mytuple = (10,25,36,8)
l = [10,25,36,8]
# print(l)
# l[1] = 100
# print(l)
""" print(mytuple)
mytuple[1] = 100
print(mytuple) """
""" for i in mytuple:
    print(i) """
    
# packing unpacking

""" myt = 1 ,20 , 25, 69 # pakcing
a, b, c, d = myt  # unpacking

print("A = ",a,"B = ",b,"C = ",c,"D = ",d) """

tp1 = (1, 2)
tp2 = (3, 4)

#tp1[2] = 100

concat_tp = tp1 + tp2

print(len(concat_tp))

# list set []
#tupe ()
#dictionary  {}
dic = {"name":"sara","bitthday":"15/02/2003","birth_city":"Rouiba"}
print(dic)
dic['name'] = "Ahmed"
print(dic)    
print(dic.values())    
print(dic.keys())    
print(dic.get("birth_city"))    











