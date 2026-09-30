class HashTable:
    def __init__(self):
        self.collection = {}
    
    def hash(self, string):
        total = sum(ord(char) for char in string)
        return total
    
    def add(self, key, value):
        hash_key = self.hash(key)
        if hash_key not in self.collection:
            self.collection[hash_key] = {}
        self.collection[hash_key][key] = value


    def remove(self, key):
        hash_key = self.hash(key)
        if hash_key in self.collection:
            if key in self.collection[hash_key]:    
                del self.collection[hash_key][key]
            if not self.collection[hash_key]:
                del self.collection[hash_key]
        else: None
    
    def lookup(self, key):
        hash_key = self.hash(key)
        if hash_key in self.collection:
            if key in self.collection[hash_key]:
                return self.collection[hash_key][key]
        else: None


table = HashTable()

table.add("sun", "Yellow")
#print(table.collection)
table.add('dear', 'friend')
table.add('read', 'book')
table.remove('sun')
print(table.lookup('pear'))
print(table.collection)
