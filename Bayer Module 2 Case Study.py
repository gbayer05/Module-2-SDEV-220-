"""
Author: Gentry 
File: Bayer Module 2 Case Study.py
Description:
This application accepts student first and last names and there GPAs, it then determines if they qualify 
for the Dean's List or Honor Roll or neither. 
"""

while True:
    last_name = input("Enter student's last name (or 'ZZZ' to quit): ")
    if last_name.upper() == "ZZZ":
        break

    first_name = input("Enter student's first name: ")
    gpa = float(input("Enter student's GPA: "))

    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")
    else:
        print(f"{first_name} {last_name} does not qualify.")
