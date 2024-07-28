print("Welcom to the tip calculator!")
total_bii = input("What was the total bii? ")
total_bii_int = float(total_bii)
percentage_tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
percentage_tip_int = float(percentage_tip)
people = input("How many people to split the bill? ")
people_int = float(people)
should_pay = ((total_bii_int * (percentage_tip_int / 100)) + total_bii_int) / people_int
print(f"Each person should pay: ${round(should_pay, 2)}")
