# display text file, line by line
file = open('countries.txt','r')

counter = 1
for line in file:
    print(str(counter) + ". " + line, end="")
    counter += 1
file.close()