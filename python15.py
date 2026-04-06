"""Write a program to accept marks of 5 students and display them in a sorted manner"""
marks = []
for i in range(5):
    mark = int(input("Enter the marks of student {}: "))
    marks.append(mark)
marks.sort()
print("The sorted marks are:", marks)
