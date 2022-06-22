print("Welcome to the ")

height = int(input("Enter your height in cm"))

if height >= 120:
    print("you can ride")
    age = int(input("Enter your age"))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("You can not ride")