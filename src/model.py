from enum import Enum
from itertools import product
import random

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class CardType(Enum):
    DRAGON = 1
    FLOWER = 2
    NUMERAL = 3
    BACK = 4 # For when dragons are returned in the reserve

class Card:
    def __init__(self, ctype, color=None, value=None):
        if ctype!=None and not isinstance(ctype, CardType):
            raise ValueError("Invalid card type provided")
        if color!=None and not isinstance(color, Color):
            raise ValueError("Invalid card color provided")
        if value!=None and not (isinstance(value, int)):
            raise ValueError("Invalid card value provided")

        self.ctype = ctype
        self.color = color
        self.value = value

    def copy(self):
        return Card(self.ctype,color = self.color, value = self.value)

    def getType(self):
        return self.ctype
    def getColor(self):
        return self.color
    def getValue(self):
        return self.value

    def __str__(self):
        return 'Card<{},{},{}>'.format(
            self.ctype.name,
            self.color.name if self.color != None else "",
            self.value if self.value!=None else "")
    def __unicode__(self):
        return unicode(str(self), "utf-8")
    def __repr__(self):
        return str(self)

class Game:
    NB_COLUMNS = 8 # number of columns
    NB_RESERVES = 3 # number of reserve slots
    NB_DRAGONS = 4 # number of identical dragon cards
    MAX_NUMERAL = 9 # maximum value of a numerical card


    def __init__(self):
        self.columns = [[] for _ in range(self.NB_COLUMNS)]
        self.reserves = [[] for _ in range(self.NB_RESERVES)]
        self.end_values = dict.fromkeys(Color,Card(CardType.NUMERAL,value=0)) # colors are put in any order...
        self.end_stacks = []
        self.flower = False
        self.cards = []

    def get_column(self,iCol):
        return self.columns[iCol].copy()
    def get_reserve(self,iR):
        return self.reserves[iR].copy()
    def get_end_stacks(self):
        return self.end_stacks.copy() + [None]*(len(Color)-len(self.end_stacks))
    def get_flower(self):
        return self.flower

    def generates(self):
        self.__init__()

        # generate the cards
        self.cards = [Card(CardType.FLOWER)]
        for color in Color:
            self.cards.extend([Card(CardType.DRAGON,color=color).copy()]*self.NB_DRAGONS)
        for color,value in set(product(Color,range(1,self.MAX_NUMERAL+1))):
            self.cards.append(Card(CardType.NUMERAL,color=color,value=value))

        random.shuffle(self.cards)

        # distribute the cards
        for i, card in enumerate(self.cards):
            iCol = (i*self.NB_COLUMNS)//(len(self.cards))
            #print(card, iCol)
            self.columns[iCol].append(card)

    def print(self):
        print("Flower :",self.flower)
        print("Reserve :",self.reserves)
        print("End stacks :",self.end_stacks)
        print("Columns :")
        #for i in range(len(self.columns)):
        #    print(i, self.columns[i])
        for i,column in enumerate(self.columns):
            print(i,column)

    def getExposedCards(self):
        exposed = []
        for col in self.columns + self.reserves:
            if len(col) != 0:
                exposed.append(col[-1])
        return exposed

    def dragons(self):
        return [] # TODO

    def auto(self):
        def isNextToDiscard(card):
            return False
            # TODO
            """
            canPut = (self.end_values.get(card.getColor()).getValue()+1 == card.getValue())
            if not canPut: return False
            for color in Color:
                if (color.value < card.getColor().value and self.end_values.get(color).getValue() < card.getValue()) or\
                   (color.value >= card.getColor().value and self.end_values.get(color).getValue() + 1< card.getValue()) :
                    return False
            return True
            """

        def autoStep():
            for x in self.columns + self.reserves:
                if len(x) == 0: continue
                card = x[-1]

                # Flower
                if card.getType() == CardType.FLOWER:
                    x.pop()
                    self.flower = True
                    return True

                # Numeral
                if card.getType() == CardType.NUMERAL and isNextToDiscard(card):
                    x.pop()
                    #self.end_values[card.getColor()] = card
                    # TODO 
                    return True

            return False
        while autoStep():
            continue
"""
game = Game()
game.generates()
game.auto()
game.print()
"""
"""
flower = Card(CardType.FLOWER)
dragon = Card(CardType.DRAGON, color = Color.RED)
numeral = Card(CardType.NUMERAL, color = Color.BLUE, value=7)
print(str(flower))
print(str(dragon))
print(str(numeral))
"""

