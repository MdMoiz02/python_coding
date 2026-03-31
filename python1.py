""" program to verify the leaf year """
year=int(input("Enter the year :")) 
if year%4 ==0:
    print(f"Entered year {year} is leaf year")
else:
    print("Entered year not a leaf year")
