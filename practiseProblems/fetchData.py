

file =  open('data.txt','w')
for i in range(1, 201):
    file.write(str(i) + '\n')
file.close()

file = open('data.txt', 'r')

for f in file:
    print(f, end = ' ')
    #print(file.readlines())

file.close()
