import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_initial_cards():
    return random.sample(cards, 2)

def calculate_score(hand):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif len(cards) == 2 and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(hand)

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    elif user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "lose, opponent has Blackjack 😱"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def blackjack_game():
    player_cards = deal_initial_cards()
    dealer_cards = deal_initial_cards()
    game_over = False    
    while not game_over:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {dealer_cards[0]}")
        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if another_card == 'y':
                player_cards.append(random.choice(cards))
            elif another_card == "n":
                game_over = True
    while dealer_score != 0 and dealer_score < 17:
            dealer_cards.append(random.choice(cards))
            dealer_score = calculate_score(dealer_cards)
    print(f"player's final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
    print(compare(user_score=player_score, computer_score=dealer_score))

def main():
    print(logo)
    while True:
        blackjack_game()
        play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if play_again == "y":
            continue
        else:
            break
if __name__ == "__main__":
    main()