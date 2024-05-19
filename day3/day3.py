name1 = input().upper().strip()
name2 = input().upper().strip()
name = name1 + name2
total1 = 0
for i in "TURE":
    total1 += name.count(i)
total2 = 0
for i in "LOVE":
    total2 += name.count(i)
score = str(total1) + str(total2)
score = int(score)
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")