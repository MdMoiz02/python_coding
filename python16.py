"""Write a program to sum a list with 4 numbers using while loop. 

"""
numbers = []
i = 0
sum = 0
while i < 4:
    num = int(input("Enter a number: "))
    numbers.append(num)
    sum+=num
print("The sum of the numbers is:", sum)
