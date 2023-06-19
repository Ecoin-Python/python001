""" str = input("please enter you word")
print(str)
str_rev = str[::-1]
if(str == str_rev):
    print("Palindrome")
else:
    print("Not Palindrome") """
    
    
numbers = 15,36,25,26,12,15,25,15,12,12,12


countes = {}

for num in numbers:
    countes[num] = countes.get(num,0) + 1
print(countes)
    

