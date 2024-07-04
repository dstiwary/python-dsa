class Node:
    def __init__(self, key,  value) -> None:
        self.key = key
        self.value = value
        self.next = None
        
class HashTable: 
    table = [None] * 10
        
    def put(self, key, value):
        offset = self.hash(key) 
        self.table[offset] = Node(key, value)
    
    def hash(self, key):
        return key % 10  
    
    def get(self, key):
        return self.table[self.hash(key)].value if self.table[self.hash(key)] is not None else None
    
    def print_hash_table(self):
        for item in self.table:
            if item is not None:
                print(item.key or None, item.value or None)
            else:
                print(None, None)
            

hash_table = HashTable()

hash_table.put(224, "BigB")
hash_table.put(620, "SmallB")
hash_table.put(533, "QueenB")

hash_table.print_hash_table()


    
