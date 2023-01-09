# 16.	Using the website https://mockaroo.com, generate a list of 500 students, 
# containing the following data: name, surname, student ID, gender, age, year 
# of study, email. Write the data to the students.json file. Then write a 
# program that creates a limited.json file with the copy of the list of students, 
# limited to data: first name, last name, student id.

import json

with open('students.json', 'r') as students:
    
    with open('limited.json', 'a') as limited:

        limited_students = []
        for student in json.load(students):
            
            copy_student = {}
            for key, value in student.items():
                
                if key in ["id","first_name","last_name"]:
                    
                    copy_student[key] = value

            limited_students.append(copy_student)
        
        json.dump(limited_students, limited, indent=6)