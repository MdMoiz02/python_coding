""".Create a tuple of integers. Ask the user for a target number, then find all pairs of numbers 
within the tuple that sum up to that target."""
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
target = int(input("Enter a target number: "))
pairs = []
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            pairs.append((numbers[i], numbers[j]))
if pairs:
    print(f"Pairs of numbers that sum up to {target}: {pairs}")
else:
    print(f"No pairs of numbers sum up to {target}.")

