print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100 # Turning into a percentage
total_tip_amount = bill * tip_as_percent # Calculating amount of tip from total bill
total_bill = bill + total_tip_amount # Adding the tip amount onto original bill to give final bill number
bill_per_person = total_bill / people # Working out how much each person pays by dividing final bill number by number of people paying
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")


