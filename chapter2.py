
# We can classify sequences by a number of ways

# container sequences
# hold a reference to the objects they contain which may be of any type
# list, tuples, collections.deque

# flat sequences
# store value of each item physically within their own memory
# limited to holding primitive values like character, bytes, numbers
# hold items of one type
# include str, bytes, bytearray, memoryview, array.array


# another way of grouping sequences is by their mutability

# mutable - list, bytearray

# immutable - strings, bytes, tuples

# container -> __contains__, __iter__, __len__
# sequence -> __getitem__, __contains__, __iter, __reversed__, index, count

# list comprehensions

# a quick way to build a sequence is using a list comprehension ( if target is a list)
# or a generator expression for all other kinds of sequences 

from collections.abc import Sequence
# class MySeq:
#     def __init__(self, data):
#         self._data = data

#     def __getitem__(self, i):
#         print(f'__getitem__({i})')
#         return self._data[i]

#     def __len__(self):
#         print('Calling __len__')
#         return len(self._data)
# s = MySeq(['a', 'b', 'c', 'd'])
# print(s.index('c'))  # This will fail

class MySeq(Sequence):
    def __init__(self, data):
        self._data = data

    def __getitem__(self, i):
        print(f'__getitem__({i})')
        return self._data[i]

    def __len__(self):
        print('Calling __len__')
        return len(self._data)
    
# task: build a list of unicode code points with the string symbols
symbols = '$¢£¥€¤'
intRepr = []
hexRepr = []
binRepr = []
# base10 repr is the broker
# character -> int then if base2: int -> base2(bin) or if base16: then int -> base16(hex)
for symbol in symbols:
    intRepr.append(ord(symbol))
    hexRepr.append(hex(ord(symbol)))
    binRepr.append(bin(ord(symbol)))
    
print(intRepr)
print(hexRepr)
print(binRepr)
b = bytes(symbols.encode('utf-8'))
print(type(b))
print(b)
print(len(b))
    