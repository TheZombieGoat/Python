"""
File:         blackjack.py
Date:         03/22/2023
"""

import random
SYMBOL_NUM = 4
VALUE_NUMS = 13
RETRIEVER_CARD = 'R*'
deck_symbols = ['\u2660', '\u2663', '\u2661', '\u2662']
deck_values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
BOX_SYMBOL = "\u2588\u2588"
numerics = ['2','3','4','5','6','7','8','9','10']

#function to make it easier to make the standard deck
def deck_maker(listA,listB):
    standard_deck = []
    for i in range(SYMBOL_NUM):
        for j in range(VALUE_NUMS):
            s = listB[j] + listA[i]
            standard_deck.append(s)
    return standard_deck

def add_and_shuffle(num_decks,num_retrievers):
    deck = deck_maker(deck_symbols,deck_values)
    for i in range(num_decks):
        deck += deck
    for i in range(num_retrievers):
        deck.append(RETRIEVER_CARD)
    random.shuffle(deck)
    return deck

def calc_value(card):
    if "J" in card or "Q" in card or "K" in card:
        return 10
    for i in range(len(numerics)):
        if numerics[i] in card:
            return int(numerics[i])

def total_value(hand):
    total = 0
    ace = []
    for i in range(len(hand)):
        if "A" in hand[i]:
            ace.append("A")
        elif hand[i] == RETRIEVER_CARD:
            return 21
        else:
            total = total + calc_value(hand[i])
    if len(ace) > 0:
        for i in range(len(ace)):
            if i == 0 and total+11 < 22:
                total = total + 11
            else:
                total = total + 1
    return total

def hit(deck,hand):
    hand.append(deck[0])
    deck.pop(0)

#checks for different possibilites (win lose etc.). Returns 0 for wins and 1 for losses and -1 for draws
def condition_check(dealer_value,player_value):
    player_difference = 21 - player_value
    dealer_difference = 21 - dealer_value
    if dealer_value == player_value:
        print("Push, no one wins.")
        return -1
    elif player_value > 21:
        print("You have busted, sorry.")
        return 1
    elif dealer_value > 21:
        print("Dealer busted, you win.")
        return 0
    elif player_difference < dealer_difference:
        if player_value == 21:
            print("Blackjack ! You win !")
            return 0
        else:
            print("You beat the dealer !")
            return 0
    elif player_difference > dealer_difference:
        print("Dealer wins.")
        return 1

def blackjack(deck,quatloos):
    hand = []
    dealer_hand = []
    for i in range(2):
        hit(deck,hand)
        hit(deck,dealer_hand)
    bet = int(input("You have "+str(quatloos)+" quatloos. How many would you like to bet? "))
    print("Dealer's hand is: ",BOX_SYMBOL, dealer_hand[1])
    if total_value(hand) != 21:
        print("Your hand is now: ",*hand,"and the total value is ",total_value(hand))
    else:
        print("Blackjack")
    while True:
        ask = input("What would you like to do? [hit/stay]: ")
        if ask.lower() == "hit":
            hit(deck,hand)
            print("Your hand is now: ",*hand,"and the total value is ",total_value(hand))
        
        if ask.lower() == "stay" or total_value(hand) >= 21:
            d_val = total_value(dealer_hand)
            player_val = total_value(hand)
            print("Dealer's hand is now",*dealer_hand,"and has value",d_val)
            results = condition_check(d_val,player_val)
            if results == 1:
                quatloos = quatloos - bet
                if quatloos <= 0:
                    return -1
            elif results == 0:
                quatloos = quatloos + bet
            replay = input("Would you like to play again? [y/yes] ")
            if replay.lower() == "y" or replay.lower() == "yes":
                return quatloos
            else:
                print("You ended the game with",quatloos,"quatloos !")
                return 0
    
def game_loop(num_decks, num_retrievers):
    quatloos = 100
    deck = add_and_shuffle(num_decks,num_retrievers)
    while quatloos > 0:
        quatloos = blackjack(deck,quatloos)
    if quatloos < 0:
        print("You're out of quatloos ! Better luck next time !")
    return 

if __name__ == '__main__':
    num_decks = int(input("How many decks of cards would you like to use? "))
    random_seed = input('What seed would you like to use? ')
    num_retrievers = int(input("How many Retriever cards would you like to add? "))
    random.seed(random_seed)
    game_loop(num_decks,num_retrievers)
