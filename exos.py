""" str = input("please enter you word")
print(str)
str_rev = str[::-1]
if(str == str_rev):
    print("Palindrome")
else:
    print("Not Palindrome") """
    
    
""" numbers = 15,36,25,26,12,15,25,15,12,12,12


countes = {}

for num in numbers:
    countes[num] = countes.get(num,0) + 1
print(countes)
numbers_list = [15,36,25,26,12,15,25,15,12,12,12]
result = list(set(numbers_list))
print(result) """

# Prime Number
n = 15 #17

if n <= 1:
    print("Flase")
# 15/2 7.5  
for i in range(2,int(n*0.5) + 1):
    if n % i == 0:
        print("False")
        
print("True")        

#print(int(7.8) +1)



    

