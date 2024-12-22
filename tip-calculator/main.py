print("Welcome to the tip calculator.")

bill_amount = float(input("What was the total bill? Rs."))

tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

no_of_people = int(input("How many people to split the bill? "))

if tip_percent == 0:
    amount_to_pay = round(bill_amount / no_of_people, 2)
else:
    new_bill_amount = bill_amount + (bill_amount * tip_percent * 0.01)
    amount_to_pay = round(new_bill_amount / no_of_people, 2)

print(f"Each person should pay: Rs.{amount_to_pay}")
