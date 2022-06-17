from scripts import CopyList
from card import Card
import random
NUMBERS_RANGE = 13
FLOWER_RANGE = 4
BOARD_NUMS = 5
DECK_NUMS = 52

class Deck:
    def __init__(self):
        self.cards = []
        self.Reset()
    
    #根據指定的牌堆來初始化
    def Set(self, cards):
        self.cards = cards

    #初始化牌堆
    def Reset(self):
        self.cards.clear()
        for i in range(NUMBERS_RANGE):
            for j in range(FLOWER_RANGE):
                self.cards.append(Card(i,j))

    #隨機發一張牌
    def Deal(self):
        randomIndex = random.randint(0,len(self.cards)-1)
        randomCard = self.cards[randomIndex]
        self.cards.pop(randomIndex)
        return randomCard

    #取得牌堆牌數
    def GetRemain(self):
        return len(self.cards)

    #複製一份Deck
    def Copy(self):
        newDeck = Deck()
        cards = CopyList(self.cards)
        newDeck.Set(cards)
        return newDeck