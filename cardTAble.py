#提供card花色數字對照表
class CardTable:
    def __init__(self):
        self.numberToString = dict()
        self.flowerToString = dict()
        self.stringToNumber = dict()
        self.stringToFlower = dict()
        self.InitNumberTable()
        self.InitFlowerTable()

    def InitNumberTable(self):
        self.numberToString = {
            0 : 'A',
            1 : '2',
            2 : '3',
            3 : '4',
            4 : '5',
            5 : '6',
            6 : '7',
            7 : '8',
            8 : '9',
            9 : '10',
            10: 'J',
            11: 'Q',
            12: 'K'
        }
        self.stringToNumber = {
            'A' : 0,
            '2' : 1,
            '3' : 2,
            '4' : 3,
            '5' : 4,
            '6' : 5,
            '7' : 6,
            '8' : 7,
            '9' : 8,
            '10': 9,
            'J' : 10,
            'Q' : 11,
            'K' : 12
        } 

    def InitFlowerTable(self):
        self.flowerToString = {
            0 : 'C',
            1 : 'D',
            2 : 'H',
            3 : 'S'
        }
        self.stringToFlower = {
            'C' : 0,
            'D' : 1,
            'H' : 2,
            'S' : 3
        }