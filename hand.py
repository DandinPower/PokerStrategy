from card import Card

#手牌結合牌面的類別
class HandWithBoard:
    def __init__(self, card, board):
        self.cards = card 
        self.board = board
        self.tempBoard = []
        self.Init()
        self.type = 0
        self.score = 0
        self.isFlush = False 
        self.isStraight = False 
        self.isFourOfAKind = False 
        self.isThreeOfAKind = False 
        self.PairNums = 0
        self.Check()

    #初始化手牌加牌面
    def Init(self):
        for i in range(5):
            self.tempBoard.append(self.board.cards[i])
        for i in range(2):
            self.tempBoard.append(self.cards[i])
        
    #檢查手牌屬性
    def Check(self):
        self.isFlush = self.IsFlush()
        self.IsStraight = self.IsStraight()
        self.IsFourOfAKind = self.IsFourOfAKind()
        self.IsThreeOfAKind = self.IsThreeOfAKind()
        self.PairNums = self.GetPairNums()

    def IsFlush(self):
        self.club = []
        self.diamond = [] 
        self.heart = [] 
        self.spade = []
        for card in self.tempBoard:
            if card.flower == 0:
                self.club.append(card)
            elif card.flower == 1:
                self.diamond.append(card)
            elif card.flower == 2:
                self.heart.append(card)
            else:
                self.spade.append(card)
        if len(self.club) >= 5:
            return True 
        if len(self.diamond) >= 5:
            return True
        if len(self.heart) >= 5:
            return True 
        if len(self.spade) >= 5:
            return True 
        return False  
        
    def IsStraight(self):
        return True

    def IsFourOfAKind(self):
        return True

    def IsThreeOfAKind(self):
        return True

    def GetPairNums(self):
        return -1

#手牌的基本類別
class Hand:
    def __init__(self, card1, card2):
        self.cards = [card1, card2]

    #比大小
    def WinLoseTie(self,hand2,board):
        handWithBoardMe = HandWithBoard(self.cards, board)
        handWithBoardOppo = HandWithBoard(hand2.cards, board)
        if handWithBoardMe.type > handWithBoardOppo.type:
            return 0
        elif handWithBoardOppo.type > handWithBoardMe.type:
            return 1
        else:
            if handWithBoardMe.score > handWithBoardOppo.score:
                return 0
            elif handWithBoardOppo.score > handWithBoardMe.score:
                return 1
            else:
                return -1