#String list tuple

list = [25,14,36,52,8,100,88,111,113]
""" mlist = []
 for num in list:
    mlist.append(num * 2)
    
print(mlist) """
# list Comprehension
#mlist = [num*2 for num in list if num > 20 and num % 2 != 0]
#print(mlist)

lang_tuple = ('english','franch','arabic','china')  # 'franch','arabic','china'

str = 'Ecoin'

#print('o' in str )

newlist = [nl for nl in lang_tuple if 'i' in nl]
print(newlist)






