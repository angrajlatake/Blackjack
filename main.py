import random

cards = ["K", "Q", "J", 9, 8, 7, 6, 5, 4, 3, 2, "A"]

users_cards = []
dealers_cards = []
def Deal_cards():
    for i in range(2):
        users_cards.append(random.choice(cards))
        dealers_cards.append(random.choice(cards))
    print(f"Your cards: {users_cards}. Your score is : {Check_total(users_cards)} \nDealer's cards: [{dealers_cards[0]}, X]")
    print(f"")
def Check_total(cards):
    total = 0
    for card in cards:
        if card == "K" or card =="J" or card == "Q":
            card = 10
        elif card == "A":
            card = 11
        total += card
    if total > 21:
        total = 0
        for card in cards:
            if card == "K" or card =="J" or card == "Q":
                card = 10
            elif card == "A":
                card = 1
            total += card
        return total

    return total

def add_card(list):
    list.append(random.choice(cards))
#Ask the user if he wants to play blackjack
start = input("Do you want to play BlackJack. y or n?")
#If yes, then clear the screen and start the game
if start == "y":
    Deal_cards()
#ask for the bet amount
user_lost = False
continue_game = True
while continue_game:
    hit = input('Do you want another card. y or n?')
    if hit == "y":
        add_card(users_cards)
        print(users_cards)
        print(f"Your score is :{Check_total(users_cards)}")
        if Check_total(users_cards) > 21:
            continue_game = False
            print("You went bust")
            user_lost = True
    else:
        continue_game = False
if not user_lost:
    print(f"Dealer's cards: {dealers_cards}")
    while Check_total(dealers_cards) < 17:
        add_card(dealers_cards)
        print(f"Drawing card. \n Dealer's Cards : {dealers_cards}")

    if Check_total(users_cards) > Check_total(dealers_cards):
        print(f"Your score is {Check_total(users_cards)} and dealer is at {Check_total(dealers_cards)}. You won!")
    elif Check_total(users_cards) == Check_total(dealers_cards):
        print("Game tied")
    else:
        print(f"Your score is {Check_total(users_cards)} and dealer is at {Check_total(dealers_cards)}. Dealer won!")

