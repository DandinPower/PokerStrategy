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
        self.IsStraight = False 
        self.IsFourOfAKind = False 
        self.IsThreeOfAKind = False 
        self.PairNums = 0
        self.Check()

    #初始化手牌加牌面
    def Init(self):
        for i in range(5):
            self.tempBoard.append(self.board[i])
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
        pass 

    def IsStraight(self):
        pass 

    def IsFourOfAKind(self):
        pass 

    def IsThreeOfAKind(self):
        pass 

    def PairNums(self):
        pass 

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