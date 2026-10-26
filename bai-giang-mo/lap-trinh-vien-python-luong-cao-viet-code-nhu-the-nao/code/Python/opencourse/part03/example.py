"""
Bài Poker / Tú lơ khơ
"""
import enum
import random


@enum.unique
class Suite(enum.Enum):
    """Chất bài (Enum)"""
    SPADE, HEART, CLUB, DIAMOND = range(4)


class Card:
    """Lá bài"""

    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __repr__(self):
        suites = '♠♥♣♦'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}'


class Poker:
    """Bộ bài"""

    def __init__(self):
        self.cards = [Card(suite, face) for suite in Suite
                      for face in range(1, 14)]
        self.current = 0

    def shuffle(self):
        """Xáo bài"""
        self.current = 0
        random.shuffle(self.cards)

    def deal(self):
        """Chia bài"""
        card = self.cards[self.current]
        self.current += 1
        return card

    @property
    def has_next(self):
        """Còn bài để chia hay không"""
        return self.current < len(self.cards)


def main():
    """Hàm chính (điểm vào của chương trình)"""
    poker = Poker()
    poker.shuffle()
    print(poker.cards)


if __name__ == '__main__':
    main()
