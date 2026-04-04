"""Write a program to find out whether a student has passed or failed if it requires a 
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
take marks as an input from the user.
"""
marks1 = float(input("Enter marks for subject 1: "))
marks2 = float(input("Enter marks for subject 2: "))
marks3 = float(input("Enter marks for subject 3: "))
total_marks = marks1 + marks2 + marks3
percentage = (total_marks / 300) * 100

if percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33:
    print("The student has passed.")
else:
    print("The student has failed.")
