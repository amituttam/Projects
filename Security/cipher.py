#!/usr/bin/env python

class Caesar:

    letters = 'abcdefghijklmnopqrstuvwxyz'
    vals = range(0,26)
    lookup = dict(zip(letters,vals))
    print lookup

    def __init__(self, key):
        if not key in range(1,26):
            raise AssertionError("Key not in range!")
        else:
            self.key = key

    def encode(self, text):
        encode = []
        for letter in text.lower():
            pos = self.lookup[letter] + self.key
            if pos > 25:
                pos = pos - 26
            encode.append(self.letters[pos])
        return ''.join(encode)

    def decode(self, text):
        decode = []
        for letter in text.lower():
            pos = self.lookup[letter] - self.key
            if pos > 25:
                pos = pos - 26
            decode.append(self.letters[pos])
        return ''.join(decode)

a = Caesar(20)
print(a.encode('HI'))
print(a.decode('BC'))
