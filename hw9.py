import numpy as np
#
# Part1
#


class Deck():

    deck_dict_suit = {"Clubs": 0, "Diamonds": 1, "Hearts": 2, "Spades": 3}
    deck_dict_rank = {"A": 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6,
                      7: 7, 8: 8, 9: 9, 10: 10, "J": 11, "Q": 12, "K": 13}

    def __init__(self):
        """Initializes the deck of cards
        >>> cards = Deck()
        >>> len(cards.deck)
        52
        >>> cards = Deck()
        >>> len(cards.dealt_cards)
        0
        >>> cards = Deck()
        >>> print(cards)
        In Deck:
        A of Clubs
        2 of Clubs
        3 of Clubs
        4 of Clubs
        5 of Clubs
        6 of Clubs
        7 of Clubs
        8 of Clubs
        9 of Clubs
        10 of Clubs
        J of Clubs
        Q of Clubs
        K of Clubs
        A of Diamonds
        2 of Diamonds
        3 of Diamonds
        4 of Diamonds
        5 of Diamonds
        6 of Diamonds
        7 of Diamonds
        8 of Diamonds
        9 of Diamonds
        10 of Diamonds
        J of Diamonds
        Q of Diamonds
        K of Diamonds
        A of Hearts
        2 of Hearts
        3 of Hearts
        4 of Hearts
        5 of Hearts
        6 of Hearts
        7 of Hearts
        8 of Hearts
        9 of Hearts
        10 of Hearts
        J of Hearts
        Q of Hearts
        K of Hearts
        A of Spades
        2 of Spades
        3 of Spades
        4 of Spades
        5 of Spades
        6 of Spades
        7 of Spades
        8 of Spades
        9 of Spades
        10 of Spades
        J of Spades
        Q of Spades
        K of Spades
        Dealt Out:
        """
        # your code here
        self.deck = [Card(rank, suit)
                     for suit in self.deck_dict_suit for rank in self.deck_dict_rank]
        self.dealt_cards = []
        return

    def shuffle(self):
        """
        This method shuffles the deck using np.random.choice
        >>> deck = Deck()
        >>> np.random.seed(5)
        >>> deck.shuffle()
        >>> print(deck.deck[:5])
        [9 of Hearts, 4 of Hearts, 7 of Spades, 7 of Diamonds, 6 of Hearts]
        >>> deck = Deck()
        >>> hand = deck.deal_cards(5)
        >>> np.random.seed(5)
        >>> deck.shuffle()
        >>> deck.deck[:5]
        [A of Spades, 9 of Hearts, Q of Spades, Q of Diamonds, J of Hearts]
        """
        # your code here
        self.deck = np.random.choice(
            self.deck + self.dealt_cards, len(self.deck + self.dealt_cards), replace=False).tolist()
        return

    def deal_cards(self, n):
        """
        This method deals out n cards and sends them all to the dealt cards list.
        It also returns the list of the cards.
        >>> cards = Deck()
        >>> cards.deal_cards(5)
        [A of Clubs, 2 of Clubs, 3 of Clubs, 4 of Clubs, 5 of Clubs]
        >>> cards = Deck()
        >>> hand = cards.deal_cards(5)
        >>> cards.deal_cards(5)
        [6 of Clubs, 7 of Clubs, 8 of Clubs, 9 of Clubs, 10 of Clubs]
        >>> cards = Deck()
        >>> hand = cards.deal_cards(5)
        >>> print(cards)
        In Deck:
        6 of Clubs
        7 of Clubs
        8 of Clubs
        9 of Clubs
        10 of Clubs
        J of Clubs
        Q of Clubs
        K of Clubs
        A of Diamonds
        2 of Diamonds
        3 of Diamonds
        4 of Diamonds
        5 of Diamonds
        6 of Diamonds
        7 of Diamonds
        8 of Diamonds
        9 of Diamonds
        10 of Diamonds
        J of Diamonds
        Q of Diamonds
        K of Diamonds
        A of Hearts
        2 of Hearts
        3 of Hearts
        4 of Hearts
        5 of Hearts
        6 of Hearts
        7 of Hearts
        8 of Hearts
        9 of Hearts
        10 of Hearts
        J of Hearts
        Q of Hearts
        K of Hearts
        A of Spades
        2 of Spades
        3 of Spades
        4 of Spades
        5 of Spades
        6 of Spades
        7 of Spades
        8 of Spades
        9 of Spades
        10 of Spades
        J of Spades
        Q of Spades
        K of Spades
        Dealt Out:
        A of Clubs
        2 of Clubs
        3 of Clubs
        4 of Clubs
        5 of Clubs
        """
        # your code here
        dealt_now = self.deck[0:5]
        self.dealt_cards += dealt_now
        self.deck = self.deck[5:]
        return dealt_now

    def __repr__(self):
        # your code here
        return "\n".join('{0}'.format(w) for w in self.deck) + "\n".join('{0}'.format(w) for w in self.dealt_cards)

    def __str__(self):
        # your code here
        return "In Deck:\n" + "\n".join('{0}'.format(w) for w in self.deck) + "\nDealt Out:" + "\n".join('{0}'.format(w) for w in self.dealt_cards)


class Card():
    '''
    This class represents a single card
    Also compares two cards

    >>> c1 = Card(4, "Clubs")
    >>> print(c1)
    4 of Clubs

    >>> c2 = Card(3, "Hearts")
    >>> print(c2)
    3 of Hearts

    >>> c1 < c2
    True

    >>> c1 > c2
    False

    >>> c1 == c2
    False
    '''
    compare_dict_suit = {"Clubs": 0, "Diamonds": 1, "Hearts": 2, "Spades": 3}
    compare_dict_rank = {"Ace": 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6,
                         7: 7, 8: 8, 9: 9, 10: 10, "Jack": 11, "Queen": 12, "King": 13}

    def __init__(self, rank, suit):
        # your code here
        self.rank = rank
        self.suit = suit
        return

    def __repr__(self):
        # your code here
        return "'%s of %s'" % (self.rank, self.suit)

    def __str__(self):
        # your code here
        return "{} of {}".format(self.rank, self.suit)

    def __eq__(self, other):
        # your code here
        if self.compare_dict_suit[self.suit] == self.compare_dict_suit[other.suit] and self.compare_dict_rank[self.rank] == self.compare_dict_rank[other.rank]:
            return True
        return False

    def __ne__(self, other):
        # your code here
        return not self.__eq__(other)

    def __lt__(self, other):
        # your code here
        if self.compare_dict_suit[self.suit] < self.compare_dict_suit[other.suit]:
            return True
        elif self.compare_dict_suit[self.suit] == self.compare_dict_suit[other.suit] and self.compare_dict_rank[self.rank] < self.compare_dict_rank[other.rank]:
            return True
        return False

    def __gt__(self, other):
        # your code here
        if self.compare_dict_suit[self.suit] > self.compare_dict_suit[other.suit]:
            return True
        elif self.compare_dict_suit[self.suit] == self.compare_dict_suit[other.suit] and self.compare_dict_rank[self.rank] > self.compare_dict_rank[other.rank]:
            return True
        return False

    def __le__(self, other):
        # your code here
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other):
        # your code here
        return self.__gt__(other) or self.__eq__(other)

#
# Part 1.2
#


class WarGame():

    def __init__(self):
        # your code here
        return

    def play_rounds(self, n=1):
        # your code here
        return

    def declare_winner(self):
        # your code here
        return

#
# Part 2
#


class BinaryTree:
    empty = ()

    def __init__(self, entry, left=empty, right=empty):
        assert(left == BinaryTree.empty or isinstance(left, BinaryTree))
        assert(right == BinaryTree.empty or isinstance(right, BinaryTree))

        self.entry = entry
        self.left = left
        self.right = right

    def is_leaf(self):
        if self.left == BinaryTree.empty and self.right == BinaryTree.empty:
            return True
        return False

    def tree_max(self):
        maxim = self.entry

        if self.left != BinaryTree.empty:
            maxim = max(maxim, self.left.tree_max())

        if self.right != BinaryTree.empty:
            maxim = max(maxim, self.right.tree_max())
        return maxim

    def tree_min(self):
        # your code here
        return

    def isBst(self):
        '''
        >>> t = BinaryTree(1, BinaryTree(1), BinaryTree(2))
        >>> t.isBst()
        False
        '''
        # your code here
        return

    def binary_search(self, elem):
        # your code here
        return
