print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")
print("5.MODULUS")
choice = int(input("Enter your choice: "))
value1 = int(input("Enter the first number: "))
value2 = int(input("Enter the second number: "))
if choice == 1:
    print("The sum is: ", value1 + value2)
elif choice == 2:
    print("The difference is: ", value1 - value2)
elif choice == 3:
    print("The product is: ", value1 * value2)
elif choice == 4:
    if value2 != 0:
        print("The quotient is: ", value1 / value2)
    else:
        print("Error: Division by zero is not allowed.")
elif choice == 5:
    if value2 != 0:
        print("The modulus is: ", value1 % value2)
    else:
        print("Error: Modulus by zero is not allowed.")
else:
    print("Invalid choice. Please select a valid operation.")
