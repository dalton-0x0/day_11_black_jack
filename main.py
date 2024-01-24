import os
import random

from art import logo, win_logo


# see readme.md for more info


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def deal_card():
    """
    A function that returns a random card from the deck.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """
    A function that takes a List of cards as input and returns the score.
    """

    # check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of
    # the actual score. 0 represents a blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # check for an ace. if the score is over 21, remove the 11 and replace it with a 1.
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    """
    Function that compares the user and computer score and returns the game result
    """

    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        print(win_logo)
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        print(win_logo)
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    """
    A function that controls the game play
    """

    print(logo)

    # deal the user and computer 2 cards each using deal_card()
    user_cards = []
    computer_cards = []
    is_game_over = False

    # initialize scores to prevent unbound errors
    user_score = 0
    computer_score = 0

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # the score will need to be rechecked with every new card drawn
    while not is_game_over:
        # if the computer or the user has a blackjack (0)
        # or if the user's score is over 21, then the game ends.
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # if the game has not ended, ask the user if they want to draw
            # another card. if yes, then use the deal_card() function to add another
            # card to the user_cards List. if no, then the game has ended.
            user_should_deal = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # let the computer play. the computer should keep drawing cards as long as it has
    # a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, "
          f"final score: {computer_score}")
    print(compare(user_score, computer_score))


# ask user if they want to restart the game
while input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()
