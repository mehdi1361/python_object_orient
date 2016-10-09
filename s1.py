from functools import partial
class Card:
    def __init__(self,rank, suit):
        self.suit = suit
        self.rank = rank
        self.hard, self.soft = self._points()
    def _points(self):
        return int(self.rank), int(self.rank)

    def show(self):
        return {'rank': self.rank, 'suit': {'symbol': self.suit.symbol, 'name': self.suit.name}}

# class NumberCard(Card):
    # def _points(self):
        # return int(self.rank), int(self.rank)

class AceCard(Card):
    def _points(self):
        return 1, 11

class FaceCard(Card):
    def _points(self):
        return 10,10

class Suit:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

def card(rank ,suit):
    if rank == 1 : return AceCard('A', suit)
    elif 2 <= rank < 11 : return Card(int(rank), suit)
    elif 11<= rank < 14 : 
        name = {11:'J', 12:'Q', 13:'K'}[rank]
        return FaceCard(name, suit)
    else:
        raise Exception('out of range')

def card_map(rank, suit):

    class_, rank_str = {1:(AceCard,'A'), 11: (FaceCard,'J'), 12: (FaceCard, 'Q'), 13: (FaceCard, 'K')}.get(str(rank), Card)
    # rank_str= {1:'A', 11:'J', 12:'Q', 13:'K'}.get(rank,str(rank))
    return class_(rank_str, suit)

def card_partial(rank, suit):
    part_class= {
            1: partial(AceCard,'A'),
            11: partial(FaceCard,'J'),
            12: partial(FaceCard,'Q'),
            13: partial(FaceCard,'K'),
    }.get(rank, partial(Card, str(rank)))
    return part_class( suit )


def deck_box():
    Club, Diamond, Heart, Spade = Suit('Club','♣'), Suit('Diamond','♦'), Suit('Heart','♥'), Suit('Spade','♠')
    deck = [ card(rank, suit)
    for suit in (Club, Diamond, Heart, Spade)
        for rank in range(1,14)
    ]
    return deck

def deck_box_map():
    Club, Diamond, Heart, Spade = Suit('Club','♣'), Suit('Diamond','♦'), Suit('Heart','♥'), Suit('Spade','♠')

    deck = [card_map(rank, suit)
    for suit in (Club, Diamond, Heart, Spade)
        for rank in range(1,14)
    ]
    return deck

def deck_map():
    Club, Diamond, Heart, Spade = Suit('Club','♣'), Suit('Diamond','♦'), Suit('Heart','♥'), Suit('Spade','♠')
    deck = [ card_partial(rank, suit)
    for suit in (Club, Diamond, Heart, Spade)
        for rank in range(1,14)
    ]
    return deck

def main():
    # print([card_deck.show() for card_deck in deck_box()][11])
    # print([card_deck.show() for card_deck in deck_box()][11])
    print([card_deck.show() for card_deck in deck_map()])


if __name__ == "__main__":
    main()
