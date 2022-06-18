import random 
from poker import Board
from deck import Deck 
from card import Card 
from hand import Hand,HandWithBoard

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

#測試手牌+Board判斷
def TestHandWithBoardIsFlush():
    board = Board()
    board.AddCard(Card(0,0))
    board.AddCard(Card(1,0))
    board.AddCard(Card(2,3))
    board.AddCard(Card(2,2))
    board.AddCard(Card(2,1))
    hand1 = Hand(Card(5,0),Card(6,0))
    hands = HandWithBoard(hand1.cards,board)
    hands.IsFlush()
    print(hands.club)
    print(hands.isFlush)

def Test():
    #TestDeal()
    #TestCopyDeck()
    #TestWhoWins()
    TestHandWithBoardIsFlush()

Test()