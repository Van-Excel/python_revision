import collections
from math import hypot

Card = collections.namedtuple("Card", "suit, rank")


class Deck:
    
    def __init__(self):
        self.ranks:list = [str(i)for i in range(2,11)] + ['J', 'Q', 'K', 'A']
        self.suits:list = "spades diamond clubs hearts".split()
        
        self.deck:list = [ Card(suit, rank) for suit in self.suits for rank in self.ranks]
        print(self.suits)
        
        
    def __len__(self) -> int:
        """
        returns the number of cards in a deck
        return type: int
        """
        print(f'the number of cards in this deck is {len(self.deck)}')
        return len(self.deck)
    
    def __getitem__(self, index) -> list:
        """_summary_
        used to retrieve a list of cards in the deck

        Returns:
            list: A list of card tuples
        """
        
        return self.deck[index]
        
        
        

deck = Deck()
print(deck[0])
len(deck)
print(f"slicing the deck: {deck[:4]}")

from random import choice
print(choice(deck))



## Implementing methods for operators

class Vector:
    def __init__(self, x:int , y:int):
        self.x = x
        self.y = y
        
        
    def __repr__(self):
        return f'Vector({self.x}, {self.y})'
    
    
    def __abs__(self):
        return hypot(self.x, self.y) #math.hypot(x, y) = √(x² + y²)
    
    def __bool__(self):
        return bool(abs(self))

        
        
    def __add__(self, anotherVec):
        x = self.x + anotherVec.x
        y = self.y + anotherVec.y
        
        return Vector(x, y)
    

v1 = Vector(2,3)
v2 = Vector(4,5)
v1 + v2
print(repr(v1))
