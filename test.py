# creating black jack

import random

CARDS = ['A ♦', 'A ♣', 'A ♥', 'A ♠',
         'J ♦', 'J ♣', 'J ♥', 'J ♠',
         'K ♦', 'K ♣', 'K ♥', 'K ♠',
         'Q ♦', 'Q ♣', 'Q ♥', 'Q ♠',
         '1 ♦', '1 ♣', '1 ♥', '1 ♠',
         '2 ♦', '2 ♣', '2 ♥', '2 ♠',
         '3 ♦', '3 ♣', '3 ♥', '3 ♠',
         '4 ♦', '4 ♣', '4 ♥', '4 ♠',
         '5 ♦', '5 ♣', '5 ♥', '5 ♠',
         '6 ♦', '6 ♣', '6 ♥', '6 ♠',
         '7 ♦', '7 ♣', '7 ♥', '7 ♠',
         '8 ♦', '8 ♣', '8 ♥', '8 ♠',
         '9 ♦', '9 ♣', '9 ♥', '9 ♠',
         '10 ♦', '10 ♣', '10 ♥', '10 ♠'
         ]

DEALER_CARDS = []
DEALER_VALUES = []

PLAYER_CARDS = []
PLAYER_VALUES = []

POUCH = [100]


# DEALING FIRST HAND
def player_hand(inp):
    r_card = random.sample(CARDS, k=int(inp))
    for cards in r_card:
        PLAYER_CARDS.append(cards)
    for items in PLAYER_CARDS:
        ti = items.split(" ")[0]
        if ti == 'A':
            PLAYER_VALUES.append(11)
        elif ti == 'Q':
            PLAYER_VALUES.append(10)
        elif ti == 'K':
            PLAYER_VALUES.append(10)
        elif ti == 'J':
            PLAYER_VALUES.append(10)

        elif ti == 'RET':
            PLAYER_VALUES.append(21)
        else:
            PLAYER_VALUES.append(int(ti))

        if 'RET 🃏' in PLAYER_CARDS:
            PLAYER_VALUES.clear()
            PLAYER_VALUES.append(21)

    print("Your cards", PLAYER_CARDS, " values", sum(PLAYER_VALUES))


def dealer_hand(inp):
    r_card = random.sample(CARDS, k=int(inp))
    for cards in r_card:
        DEALER_CARDS.append(cards)
    for items in DEALER_CARDS:
        ti = items.split(" ")[0]
        if ti == 'A':
            DEALER_VALUES.append(11)
        elif ti == 'Q':
            DEALER_VALUES.append(10)
        elif ti == 'K':
            DEALER_VALUES.append(10)
        elif ti == 'J':
            DEALER_VALUES.append(10)

        elif ti == 'RET':
            DEALER_VALUES.append(21)
        else:
            DEALER_VALUES.append(int(ti))

    if 'RET 🃏' in PLAYER_CARDS:
        DEALER_VALUES.clear()
        DEALER_VALUES.append(21)


# print("THE DEALER", DEALER_CARDS, " values", sum(DEALER_VALUES))


# DEALING SECOND HAND
def player_deal():
    r_card = random.sample(CARDS, k=int(1))
    for card in r_card:
        ti = card.split(" ")[0]
        if ti == 'A':
            user_inp = input("do you want A to be 1 or 11")
            if int(user_inp) == 1:
                print("A is equal to 1")
                PLAYER_VALUES.append(1)
            else:
                print("A is equal to 11")
                PLAYER_VALUES.append(11)
        elif ti == 'Q':
            PLAYER_VALUES.append(10)
        elif ti == 'K':
            PLAYER_VALUES.append(10)
        elif ti == 'J':
            PLAYER_VALUES.append(10)
        elif ti == 'RET':
            PLAYER_VALUES.append(21)

        else:
            PLAYER_VALUES.append(int(ti))
        PLAYER_CARDS.append(card)

    if 'RET 🃏' in PLAYER_CARDS:
        PLAYER_VALUES.clear()
        PLAYER_VALUES.append(21)


#  print("player deal", PLAYER_VALUES)


def dealer_deal():
    r_card = random.sample(CARDS, k=int(1))
    for card in r_card:
        ti = card.split(" ")[0]
        if ti == 'A':
            user_inp = input("do you want A to be 1 or 11")
            if int(user_inp) == 1:
                print("A is equal to 1")
                DEALER_VALUES.append(1)
            else:
                print("A is equal to 11")
                DEALER_VALUES.append(11)
        elif ti == 'Q':
            DEALER_VALUES.append(10)
        elif ti == 'K':
            DEALER_VALUES.append(10)
        elif ti == 'J':
            DEALER_VALUES.append(10)

        elif ti == 'RET':
            DEALER_VALUES.append(21)
        else:
            DEALER_VALUES.append(int(ti))
        DEALER_CARDS.append(card)

    if 'RET 🃏' in PLAYER_CARDS:
        DEALER_VALUES.clear()
        DEALER_VALUES.append(21)


#  print("DEALER deal", DEALER_VALUES)


# Launch game
def game_loop():
    inp = input("how many deck of cards would you like?: ")
    seed = str(input("What seed would you like to use? "))
    random.seed(seed)

    # how many retrievers present
    retriever = input('How many retrievers do you want to add?: ')

    for _ in range(int(retriever)):
        CARDS.append("RET 🃏")
    # print(CARDS)
    print(f"you have {POUCH}  quatloos")
    bet = input("how much quatloos would you like to bet?: ")

    for amount in POUCH:
        new_price = int(amount) - int(bet)
        POUCH[0] = new_price
        # don't touch this for real just don't
    print(f"you bet {int(bet)} quatloos, you have {POUCH} left ")

    player_hand(inp)
    dealer_hand(inp)

    inp2 = input('do you want to hit or stay? ').lower()
    if inp2 == 'hit':
        player_deal()
    elif inp2 == 'stay':
        pass
    # print(PLAYER_VALUES)
    print("YOUR HAND", PLAYER_CARDS, " values", sum(PLAYER_VALUES))

    'DEALING SECOND HAND OR FAULT FOR DEALER'
    choice = ['DEAL', 'HALT']
    choose = random.choice(choice)

    if choose == 'DEAL':
        dealer_deal()
    print("Dealer's hand", DEALER_CARDS, " values", sum(DEALER_VALUES))

    sum_dealer = sum(DEALER_VALUES)
    sum_player = sum(PLAYER_VALUES)

    minimum_p = sum_player - 21
    minimum_d = sum_dealer - 21

    if sum_player > 21 and sum_dealer < 21:
        print("player bust dealer wins")
        print(f"You have {POUCH} left ")

    elif sum_dealer and sum_player == 21:
        print("draw")
        print(f"You have {POUCH} left ")

    elif sum_player == 21:
        print("dealer bust player wins")
        print("you have blackjack")
        for amount in POUCH:
            new_price = int(amount) + int(bet) * 2
            POUCH[0] = new_price
        print(f"You have {POUCH} left ")

    elif sum_dealer > 21 and sum_player < 21:
        print("dealer bust player wins")
        for amount in POUCH:
            new_prices = int(amount) + int(bet) * 2
            POUCH[0] = new_prices
        print(f"You have {POUCH} left ")

    elif sum_dealer == 21:
        print("player bust dealer wins")
        print(f"You have {POUCH} left ")

    elif sum_player and sum_dealer > 21:
        print("both bust try again")

    elif minimum_p > minimum_d:
        print("dealer bust player wins")
        print("you have blackjack")
        for amount in POUCH:
            new_price = int(amount) + int(bet) * 2
            POUCH[0] = new_price
        print(f"You have {POUCH} left ")

    elif minimum_d > minimum_p:
        print("player bust dealer wins")
        print(f"You have {POUCH} left ")

    elif sum_dealer == sum_player:
        print("draw")
        print(f"You have {POUCH} left ")


# refactor loop game
while True:
    game_loop()
    re_try = input("do you want to play again (y)/(n)? ").lower()
    if re_try == "y":
        DEALER_CARDS.clear()
        DEALER_VALUES.clear()
        PLAYER_CARDS.clear()
        PLAYER_VALUES.clear()
        game_loop()

    else:
        print(f"You have ended the game with {POUCH} quatloos")
