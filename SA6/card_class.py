# Author: Alexander Marcoux
# Date: 13 February 2023
# Purpose: creating a card class

class Card:
    def __init__(self, card_number, suit_value):
        self.cn = card_number
        self.sv = suit_value

    # assigning suit based on the numerical value given (1-4)
    def __str__(self):
        if self.sv == 1:
            suit = "clubs"
        elif self.sv == 2:
            suit = "spades"
        elif self.sv == 3:
            suit = "diamonds"
        elif self.sv == 4:
            suit = "hearts"

        if self.cn == 11:
            self.cn = "Jack"
        elif self.cn == 12:
            self.cn = "Queen"
        elif self.cn == 13:
            self.cn = "King"

        return str(self.cn) + " of " + str(suit)
