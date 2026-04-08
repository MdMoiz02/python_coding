"""Given a list of numbers (including negatives), create a new list containing the squares of each number, sorted in ascending order and list comprehension."""
def sorted_squares(nums):
    return sorted([x**2 for x in nums])
numbers = [-4, -1, 0, 3, 10]
result = sorted_squares(numbers)    
print("The list of squared numbers sorted in ascending order is:", result)
