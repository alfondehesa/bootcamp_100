# Bill tip calculator

bill = float(input("What is the bill: "))
pax = float(input("How many people are sharing the bill: "))
percent_tip = float(input("What tip percent would you like to give (12, 15 or 18): "))

tpp = (bill * ((percent_tip / 100) + 1)) / pax

print(f"Each person should pay ${tpp} .")
