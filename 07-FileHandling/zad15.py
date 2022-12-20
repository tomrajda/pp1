# 15.	Find any text file on the Internet that contains at least 30 lines of 
# text and download that file to your computer. Then write a program that 
# displays the first five lines from the file and then waits for the Enter 
# key to be pressed. Then repeat displaying the next five lines from the file, 
# waiting for the Enter key to be pressed each time.


with open("sample3.txt", "r") as file:
    
    lines = file.readlines()

    counter = 0
    no = 1
    for line in lines:
        print(str(no) + ". " + line[:-1])
        counter += 1
        no += 1
        if counter % 5 == 0:
            message = input("\nType enter to display next 5 lines of text\n")
        
    
 


