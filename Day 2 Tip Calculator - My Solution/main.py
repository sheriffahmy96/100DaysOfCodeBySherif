#If the bill was $150.00, split between 5 people, with 12% tip. 
#Format the result to 2 decimal places = 33.60


print("Welcome to the tip calculator!")
bill = round(float(input("What was the total bill?\n$")), 2)
tip = (float(input("What percentage tip would you like to give?\n%")))/ 100 + 1
people = int(input("How many people to split the bill?\n"))
Total = print(f"Each person should pay: {'{:.2f}'.format(bill / people * tip , 2)}") 
