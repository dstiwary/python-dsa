class Node:
    def __init__(self, key,  value) -> None:
        self.key = key
        self.value = value
        self.next = None
        
class HashTable: 
    table = [None] * 10
        
    def put(self, key, value):
        #~^ Get the offset for the key
        offset = self.hash(key)
                
        check_node_value = self.get(key)
        
        # if the value already exists 
        if check_node_value is not None: 
            # ~^ Get the initial node 
            current_node = self.table[offset] 
            while current_node is not None: 
                if current_node.key == key:
                    current_node.value = value
                current_node = current_node.next
        else:
            new_node = Node(key, value)
            new_node.next = self.table[offset]
            self.table[offset] = new_node
            
        
    
    def hash(self, key):
        return key % len(self.table)
    
    def get(self, key):
        # return self.table[self.hash(key)].value if self.table[self.hash(key)] is not None else None
        offset = self.hash(key)
        current_entry = self.table[offset]
        
        while current_entry is not None: 
            if current_entry.key == key:
                return current_entry.value
            current_entry = current_entry.next 
        return None
    
    def remove(self, key):
        offset = self.hash(key)
        previous = self.table[offset]
        current = self.table[offset]
        while previous is not None:
            if current.key == key:
                if current == self.table[offset]:
                    self.table[offset] = self.table[offset].next
                else: 
                    previous.next = current.next
                return True
            previous = current
                    
        
    
    def print_hash_table(self):
        count = 0 
        output = ""
        for item in self.table:
            if item is not None:
                offset = self.hash(item.key) 
                output += f"\n {count}:{offset}:"
                entry = self.table[offset]
                while entry is not None:
                    output += f"{entry.key}:{entry.value} "
                    entry = entry.next
            else:
                output += f"\n {count}:{None}:{None}"
            count +=1 
        print(output) 

hash_table = HashTable()

hash_table.put(224, "BigB")
hash_table.put(620, "SmallB")
hash_table.put(533, "QueenB")
hash_table.put(814, "MomB")
hash_table.put(334, "LatestMomB")
# hash_table.remove(224)


hash_table.print_hash_table()