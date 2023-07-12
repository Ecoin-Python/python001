# open file
# write to file
# read from file
# close file
# r = read    w = write x = excute  a = append 
myfile = open("ecoin.txt",'r')
#myfile.write("\t\nWelcom to Python")

print(myfile.read(7))

myfile.close()