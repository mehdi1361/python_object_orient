import random
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

class CardFactory:
    def rank(self, rank):
        self.class_, self.rank_str = {
                1: (AceCard, 'A'),
                11: (FaceCard, 'J'),
                12: (FaceCard,'Q'),
                13: (FaceCard, 'K'),
        }.get(rank, (Card, str(rank)))
        return self

    def suit(self, suit):
        return self.class_(self.rank_str, suit)

class Deck:
    def __init__(self):
        self._card_factory = CardFactory()
        self.Club, self.Diamond, self.Heart, self.Spade = Suit('Club','♣'), Suit('Diamond','♦'), Suit('Heart','♥'), Suit('Spade','♠')
        self._cards = [self._card_factory.rank(r).suit(s) for r in range(1,13) for s in (self.Club, self.Diamond, self.Heart, self.Spade)]
        random.shuffle(self._cards)

    def pop(self):
        return self._cards.pop()

class Deck2(list):
    def __init__(self):

        self._card_factory = CardFactory()
        self.Club, self.Diamond, self.Heart, self.Spade = Suit('Club','♣'), Suit('Diamond','♦'), Suit('Heart','♥'), Suit('Spade','♠')
        super().__init__(self._card_factory.rank(r).suit(s) for r in range(1,13) for s in (self.Club, self.Diamond, self.Heart, self.Spade))
        random.shuffle(self)


class Hand:
    def __init__(self, dealer_card):
        self.dealer_card = dealer_card
        self.cards = []

    def hard_total(self):
        return sum(c.hard for c in self.cards)

    def soft_total(self):
        return sum(c.soft for c in self.cards)
      
    def hand_cards(self):
        return [c.show() for c in self.cards]

# def main():
    # card = CardFactory()
    # Club, Diamond, Heart, Spade = Suit('Club','♣'), Suit('Diamond','♦'), Suit('Heart','♥'), Suit('Spade','♠')
    # deck = [card.rank(r).suit(s) for r in range(1,13) for s in (Club, Diamond, Heart, Spade)]
    # random.shuffle(deck)
    # hand = [deck.pop(), deck.pop()]
    # print([i.show() for i in hand])
    # # print([deck_item.show() for deck_item in deck])


# def main():
    # deck = Deck()
    # hand = [deck.pop(), deck.pop()]
    # print([i.show() for i in hand])

# def main():
    # deck = Deck2()
    # hand = [deck.pop(), deck.pop()]
    # print([i.show() for i in hand])

def main():
    deck = Deck2()
    hand = Hand(deck.pop())
    hand.cards.append(deck.pop())
    hand.cards.append(deck.pop())

    print('sum hard_total: %s and sum soft_total: %s and cards: %s' % (hand.hard_total(), hand.soft_total(), hand.hand_cards()))


if __name__ == "__main__":
    main()
