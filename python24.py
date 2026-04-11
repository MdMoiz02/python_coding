"""Write a program that takes a list with duplicate elements and returns a new list with only the unique elements, keeping the original order."""
def unique_elements(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list
input_list = [1, 2, 3, 2, 4, 1, 5]
result = unique_elements(input_list)
print(result) 
