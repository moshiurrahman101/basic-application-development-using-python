file = open("myfile.txt", "rt")



i = 0
for x in file.readlines(): 
    if(i>1):
        break
    print(x)
    i += 1

