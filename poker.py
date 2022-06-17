import random
from scripts import CopyList
from scripts import nGetM
from deck import Deck
from hand import Hand
NUMBERS_RANGE = 13
FLOWER_RANGE = 4
BOARD_NUMS = 5
DECK_NUMS = 52

#牌面的類別
class Board:
    def __init__(self):
        self.cards = []
    
    #新增一張牌到牌面
    def AddCard(self, card):
        if len(self.cards) >= 5:
            print('Board is Full!')
        else:
            self.cards.append(card)
    
    #取得牌面的張數
    def GetCardsNums(self):
        return len(self.cards)

    #判斷這個牌面以及兩手牌的勝率為何
    def WhoWins(self, deck, hand1, hand2):
        tempDeck = deck.Copy()
        hand1Cards = hand1.cards 
        hand2Cards = hand2.cards 
        numsOfCardsNeedToDraw = BOARD_NUMS - self.GetCardsNums()
        tempRemainDeck = tempDeck.cards 
        
        posibility = nGetM(len(tempRemainDeck), numsOfCardsNeedToDraw)
        for index in posibility:
            tempBoard = CopyList(self.cards)
            for i in range(len(index)):
                if index[i] == 1:
                    tempBoard.append(tempRemainDeck[i])
            #tempBoard為當前可能性
