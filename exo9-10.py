#list = [15,25,3,99,88,45]
""" list = [15,25,3,99,88,45]
print(list)
slist = sorted(list)
print(slist) """
#fibonacci
#01234567
#7   ===>  01123354759611713

#0+1  == 1  1+2 => 3   2+3 ==> 5
num = input('please enter num')
num = int(num)
#0 1 1 2 3 5 8 4 5 6
sequence = [0,1]  # len  sequence[-2]
# [0, 1, 1, 2, 3, 5, 8]
while len(sequence) < num:
    next_num = sequence[-1] + sequence[-2]
    sequence.append(next_num)
print(sequence)


