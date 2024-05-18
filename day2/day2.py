print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
if size == "S":
    total = 15
elif size == "M":
    total = + 20
elif size == "L":
    total = 25
add_pepperoni = input()
if add_pepperoni == "Y":
    if size == "S":
        total = total + 2
    elif size in ["M","L"]:
        total = total + 3
extra_cheese = input()
if extra_cheese == "Y":
    total = total + 1
print(f"Your final bill is: ${total}.")