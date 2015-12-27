class HashTable:

    def __init__(self):
        self.size = 11
        self.slots = [None]*self.size
        self.data = [None]*self.size

    def hashfunction(self, key, size):
        return key%size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.data[hashvalue] == None:
            self.slots[hashvalue] == key
            self.data[hashvalue] == data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] == data
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslots] != key:
                    nextslot = self.rehash(hashvalue, len(self.slots))

                if self.data[nextslot] == None:
                    self.slots[nextslot] == key
                    self.data[nextslot] == data
                else:
                    if self.slots[nextslot] == key:
                        self.data[nextslot] == data

