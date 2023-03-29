# Author: Alexander Marcoux
# Date: 13 February 2023
# Purpose: creating a deck class
from random import randint


class Deck:
    def __init__(self):
        self.card_list = []

    # adding 52 cards (4 sets of 13 cards) into the deck
    def add_standard_cards(self):
        for i in range(0, 4):
            for num in range(1, 14):
                self.card_list.append(num)

    # shuffling the deck by placing cards in random positions w/in the deck
    def shuffle(self):
        for i in range(0, len(self.card_list)):
            min = 0
            max = len(self.card_list) - 1  # - 1 to account for the fact that index starts at 0
            random_pos = randint(min, max)

            temp = self.card_list[i]
            self.card_list[i] = self.card_list[random_pos]
            self.card_list[random_pos] = temp

    # using .pop() to take the last "n" number of cards from the deck
    def deal(self, n):
        hand = Deck()

        for i in range(0, n):
            hand.card_list.append(self.card_list.pop())

        return hand
