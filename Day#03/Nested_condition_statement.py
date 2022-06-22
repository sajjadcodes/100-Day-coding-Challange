print("Welcome to the ")

height = int(input("Enter your height in cm"))

if height >= 120:
    print("you can ride")
    age = int(input("Enter your age"))
    if age >=18:
        print("Please pay 20$")
    else:
        print("Please pay 10$")
else:
    print("You can not ride")
    