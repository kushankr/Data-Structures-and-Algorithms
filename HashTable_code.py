# HashTable is impleneted as 'dict' in python
# Search, Insertion, Deletion - all O(1)


class HashTable:
    def __init__(self):
        self.size = 11
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def put(self, key, value):
        hashvalue = self.hashing(key)

        if self.keys[hashvalue] is None:
            self.keys[hashvalue] = key
            self.values[hashvalue] = value
        else:
            if self.keys[hashvalue] == key:
                self.values[hashvalue] = value
            else:
                rehashvalue = self.rehashing(hashvalue)
                while self.keys[rehashvalue] is not None and self.keys[rehashvalue] != key:
                    rehashvalue = self.rehashing(rehashvalue)

                if self.keys[rehashvalue] == key:
                    self.values[rehashvalue] = value
                if self.keys[rehashvalue] is None:
                    self.keys[rehashvalue] = key
                    self.values[rehashvalue] = value

    def get(self, key):
        hashvalue = self.hashing(key)

        if self.keys[hashvalue] == key:
            return self.values[hashvalue]
        else:
            rehashvalue = self.rehashing(hashvalue)
            while self.keys[rehashvalue] != key and rehashvalue != hashvalue:
                rehashvalue = self.rehashing(rehashvalue)

            if rehashvalue == hashvalue:
                return 'Not present'
            if self.keys[rehashvalue] == key:
                return self.values[rehashvalue]

    def rehashing(self, key):
        return (key + 1) % self.size

    def hashing(self, key):
        return key % self.size


mydict = HashTable()
mydict.put(113, 'a')
mydict.put(117, 'b')
mydict.put(97, 'c')
mydict.put(100, 'd')
mydict.put(114, 'e')
mydict.put(108, 'f')
mydict.put(116, 'g')
mydict.put(105, 'h')
mydict.put(99, 'i')

print mydict.keys

print mydict.get(108)

mydict.put(108, 'kush')

print mydict.keys
print mydict.values

print mydict.get(108)

print mydict.get(10000)
