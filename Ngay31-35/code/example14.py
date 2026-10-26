"""
Hướng đối tượng
Enum - Khi giá trị của một biến chỉ có số lựa chọn hữu hạn, kiểu thích hợp nhất là enum
Thông qua enum chúng ta có thể định nghĩa các hằng số biểu tượng, hằng số biểu tượng tốt hơn hằng số kiểu tường minh (literal)
"""
from enum import Enum, unique

import random


@unique
class Suite(Enum):
    """Chất bài (Enum)"""
    SPADE, HEART, CLUB, DIAMOND = range(4)

    def __lt__(self, other):
        return self.value < other.value


class Card():
    """Lá bài"""
    
    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        suites = ('♠️', '♥️', '♣️', '♦️')
        faces = ('', 'A', '2', '3', '4', '5', '6', 
                 '7', '8', '9', '10', 'J', 'Q', 'K')
        return f'{suites[self.suite.value]} {faces[self.face]}'


class Poker():
    """Bộ bài"""
    
    def __init__(self):
        self.index = 0
        self.cards = [Card(suite, face)
                      for suite in Suite
                      for face in range(1, 14)]

    def shuffle(self):
        """Xáo bài"""
        self.index = 0
        random.shuffle(self.cards)

    def deal(self):
        """Chia bài"""
        card = self.cards[self.index]
        self.index += 1
        return card

    @property
    def has_more(self):
        """Còn bài hay không"""
        return self.index < len(self.cards)


class Player():
    """Người chơi"""

    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_card(self, card):
        """Rút bài"""
        self.cards.append(card)

    def arrange(self):
        """Xếp bài trên tay"""
        self.cards.sort(key=lambda card: (card.suite, card.face))


def main():
    """Hàm chính"""
    poker = Poker()
    poker.shuffle()
    players = [
        Player('Đông Tà'), Player('Tây Độc'), 
        Player('Nam Đế'), Player('Bắc Cái')
    ]
    while poker.has_more:
        for player in players:
            player.get_card(poker.deal())
    for player in players:
        player.arrange()
        print(player.name, end=': ')
        print(player.cards)


if __name__ == '__main__':
    main()
