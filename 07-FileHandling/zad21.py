# 21.	Create a program that saves to a text file, numbers in the range 
# of <1,10> with their second and third power. Sample result:
# 1,1,1
# 2,4,8
# 3,9,27
# 4,16,64

with open("power_numbers.txt", "w") as file:
    for i in range(11):
        line = ""
        for j in range(1,4):
            line += str(i ** j) + ","
        
        file.writelines(line[:-1]+"\n")
