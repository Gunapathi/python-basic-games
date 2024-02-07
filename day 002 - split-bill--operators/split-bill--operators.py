total = float(input("What was the total bill? $"))
totalPeople = int(input("How many people to split the bill? "))
tip = int(input("Percentage of Tip? 10, 12 or 15? "))


print(f"Each person should pay: ${((total + (total * (tip / 100))) / totalPeople)}")