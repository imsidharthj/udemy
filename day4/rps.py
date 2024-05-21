import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rps = [rock, paper, scissors]
# user_rps = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n").strip()
# computer_rps = random.choice(rps)
# if user_rps == "0" and computer_rps == scissors:
#     print(f"{rock}\n Computer chose: \n {computer_rps}\nYou Win")
# elif user_rps == "0" and computer_rps == paper:
#     print(f"{rock}\n Computer chose: \n {computer_rps}\nYou Lose")
# elif user_rps == "1" and computer_rps == scissors:
#     print(f"{paper}\n Computer chose: \n {computer_rps}\nYou Lose")
# elif user_rps == "1" and computer_rps == rock:
#     print(f"{paper}\n Computer chose: \n {computer_rps}\nYou Win")
# elif user_rps == "2" and computer_rps == rock:
#     print(f"{scissors}\n Computer chose: \n {computer_rps}\nYou Lose")
# elif user_rps == "2" and computer_rps == paper:
#     print(f"{scissors}\n Computer chose: \n {computer_rps}\nYou Win")
# elif user_rps == computer_rps:
#     print("It's a tie!")
user_rps = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: \n").strip())
computer_choice = rps[random.randint(0, 2)]
print(f"You chose: {rps[user_rps]}")
print(f"Computer chose: {computer_choice}")

if user_rps == computer_choice:
    print("It's a tie!")
elif(user_rps == 0 and computer_choice == 2) or \
    (user_rps == 1 and computer_choice == 0) or \
    (user_rps == 2 and computer_choice == 1):
        print("You win!")
else:
        print("You lose!")