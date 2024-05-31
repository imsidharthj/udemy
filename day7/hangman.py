import random
from hangman_draw import word_list, stages, logo
# from test_main import stages
# from test_main import logo
chosen_word = random.choice(word_list)
print(chosen_word)
display = ["_" for _ in chosen_word]
lives = 6
print(logo)
while "_" in display:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print("Already Guessed The Letter",guess)
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives = lives - 1
        if lives == 0:
            print(f"{display}{stages[6]}")
            print("You Lose")
            break
    print(display)
    print(stages[6-lives])
    if "_" not in display:
        print(f"You Win \n You've guessed the word {chosen_word} correctly")