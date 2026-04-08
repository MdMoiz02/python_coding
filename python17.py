"""Write a program to sum a list with 4 numbers using while loop."""
numbers = [1, 2, 3, 4]
total = 0
i = 0
while i < len(numbers):
    total += numbers[i]
    i += 1
print("The sum of the numbers is:", total) 
