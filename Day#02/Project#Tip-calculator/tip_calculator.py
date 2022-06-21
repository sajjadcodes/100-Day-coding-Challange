print("Welcome to the tip calculator!")
bill = input("What was the total bill?$ ")
tip_percent = input("What percentage tip would you like to give? 10, 12, or 15? ")
total_people = input("How many people to split the bill?")

tip_amount = (float(tip_percent) /100) * float(bill)
total_bill = float(bill) + tip_amount
each_person = total_bill / int(total_people)
final_amount = "{:.2f}".format(each_person)
print(f"Each person should pay: {final_amount }")