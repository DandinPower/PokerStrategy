from cardTAble import CardTable
class Card:
    def __init__(self, number, flower):
        self.number = number  # 0 -> A, 12 -> K
        self.flower = flower  # 0, 1, 2, 3 ;梅花, 磚塊, 愛心, 黑桃
        self.table = CardTable()
    
    #印出牌
    def __str__(self):
        number = self.table.numberToString[self.number]
        flower = self.table.flowerToString[self.flower]
        return f'{number}{flower}'