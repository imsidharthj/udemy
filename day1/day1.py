bill = float(input("What was totoal bill? $"))
n = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))
split_bill = (((n + 100)/100) * bill) / people
split_bill = round(split_bill, 2)
print(f"Each person should pay: ${split_bill:.2f}")