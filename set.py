my_set = {100,200,300,400,500,600}
print(my_set)
my_set.add(700)
print(my_set)
my_set.remove(500)
print(my_set)

for num in my_set:
    print(num)


if(900 in my_set):
    print("Yes ")
else:
    print("No")
