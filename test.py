import random 
from poker import *

#測試發牌對deck的操作
def TestDeal():
    deck = Deck()
    for i in range(52):
        print(deck.GetRemain())
        card = deck.Deal()
        print(card)

#測試複製deck物件
def TestCopyDeck():
    deck = Deck()
    tempDeck = deck.Copy()
    print(deck.GetRemain())
    tempDeck.Deal()
    print(deck.GetRemain())

#測試牌面加兩手牌誰勝誰負
def TestWhoWins():
    deck = Deck()
    board = Board()
    hand1 = Hand(deck.Deal(),deck.Deal())
    hand2 = Hand(deck.Deal(),deck.Deal())
    board.WhoWins(deck, hand1, hand2)

def Test():
    #TestDeal()
    #TestCopyDeck()
    TestWhoWins()

Test()