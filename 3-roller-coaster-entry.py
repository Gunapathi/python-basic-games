print("Welcome to the roller coaster")
height = int(input("What is your height "))

if height >= 120:
    age = int(input("What is your age "))
    if age < 12:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry, you cannot ride")