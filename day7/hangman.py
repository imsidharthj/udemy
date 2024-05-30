import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display = ["_" for _ in chosen_word]
while "_" in display:
    guess = input().lower()
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = letter
    print(display)